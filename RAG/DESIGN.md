# RAG against the machine — 設計書

## 1. 目的とスコープ

vLLM リポジトリを対象に、自然言語の質問に対して関連ソース箇所を取得し、LLM で回答を生成する RAG システムを構築する。

**性能目標（mouli準拠）**

| 指標 | 目標値 |
| --- | --- |
| 索引付け時間 | ≤ 5 分 |
| コールドスタート遅延 | ≤ 60 秒 |
| ウォーム取得 1000 問 | ≤ 90 秒 |
| Recall@5 (docs) | ≥ 80% |
| Recall@5 (code) | ≥ 50% |

---

## 2. 全体アーキテクチャ

```
┌────────────────────────────────────────────────────────┐
│                     CLI (Python Fire)                  │
│  index │ search │ search_dataset │ answer │ ...        │
└────────────┬──────────────┬──────────────┬─────────────┘
             │              │              │
        ┌────▼─────┐   ┌────▼─────┐  ┌─────▼──────┐
        │ Ingestion│   │ Retrieval│  │ Generation │
        │  - walk  │   │ - BM25   │  │ - Qwen3    │
        │  - chunk │   │ - top-k  │  │ - prompt   │
        │  - index │   │          │  │ - parse    │
        └────┬─────┘   └────┬─────┘  └─────┬──────┘
             │              │              │
        ┌────▼──────────────▼──────────────▼─────┐
        │   Storage (data/processed/)            │
        │   chunks/*.jsonl  bm25_index/*.pkl     │
        └────────────────────────────────────────┘
                          ▲
                          │
                  ┌───────┴────────┐
                  │   Evaluation   │
                  │  Recall@k      │
                  └────────────────┘
```

レイヤーは I/O・ロジック・モデルを分離する：

- **Ingestion**: ファイル走査 → チャンク化 → 索引保存
- **Retrieval**: クエリ → BM25 スコアリング → top-k
- **Generation**: 文脈組立 → Qwen3 推論 → JSON 整形
- **Evaluation**: 取得結果 ↔ 正解の重なり計算

---

## 3. ディレクトリ構成

```
RAG/
├── pyproject.toml
├── uv.lock
├── Makefile
├── README.md
├── DESIGN.md
├── .gitignore
├── data/
│   ├── raw/                # vllm-0.10.1/
│   ├── processed/          # 生成（gitignore）
│   │   ├── chunks/
│   │   │   ├── code.jsonl
│   │   │   └── docs.jsonl
│   │   └── bm25_index/
│   │       ├── code.pkl
│   │       └── docs.pkl
│   ├── datasets/           # AnsweredQuestions / UnansweredQuestions
│   └── output/             # 生成（gitignore）
└── src/student/
    ├── __init__.py
    ├── __main__.py         # Fire エントリポイント
    ├── cli.py              # CLI コマンド束ね
    ├── models.py           # pydantic モデル
    ├── config.py           # 定数・パス
    ├── ingestion/
    │   ├── __init__.py
    │   ├── walker.py       # ファイル列挙・分類
    │   ├── chunker.py      # ベース + Python/Text 実装
    │   └── indexer.py      # BM25 索引構築・保存
    ├── retrieval/
    │   ├── __init__.py
    │   ├── retriever.py    # 索引ロード + 検索
    │   └── ranker.py       # スコア統合・重複除去
    ├── generation/
    │   ├── __init__.py
    │   ├── llm.py          # Qwen3 ローダ（シングルトン）
    │   └── prompt.py       # プロンプトテンプレート
    └── evaluation/
        ├── __init__.py
        └── recall.py       # Recall@k 計算
```

---

## 4. データモデル（pydantic）

`src/student/models.py` に subject 指定のモデルを実装。拡張用に内部モデルを追加する：

```python
class Chunk(BaseModel):
    chunk_id: str            # uuid4
    file_path: str           # vllm-0.10.1 からの相対 or 完全パス
    first_character_index: int
    last_character_index: int
    text: str
    kind: Literal["code", "docs"]
```

外部 IO に出すのは `MinimalSource` / `MinimalSearchResults` / `MinimalAnswer` / `StudentSearchResults` / `StudentSearchResultsAndAnswer`。`Chunk` は内部表現で、JSON 出力時は `MinimalSource` に射影する。

---

## 5. Ingestion 設計

### 5.1 ファイル分類（walker）

| 種別 | 拡張子 | チャンカ |
| --- | --- | --- |
| code | `.py` | PythonChunker |
| docs | `.md`, `.rst`, `.txt` | TextChunker |
| skip | バイナリ、`__pycache__`、`.git`、テスト固定データ等 | — |

ファイルは UTF-8 読込、`errors="replace"` で堅牢化。

### 5.2 チャンキング戦略

共通契約：

```python
class Chunker(Protocol):
    def split(self, text: str, file_path: str) -> list[Chunk]: ...
```

**PythonChunker**

- `ast.parse` で関数・クラス・モジュールトップを単位に分割。
- 1 ノードが `max_chunk_size`（既定 2000 文字）超過ならスライディングウィンドウで分割（overlap ≈ 200 文字）。
- 各チャンクは元ファイル内の `first/last_character_index` を保持。
- 解析失敗時はテキストチャンカへフォールバック。

**TextChunker**

- Markdown 見出し（`#`～`###`）境界を優先に分割。
- 見出し単位が 2000 超なら段落（空行）→ 文（句点）→ 文字、の順で再帰分割。
- overlap は 100 文字程度（文脈保持と recall のトレードオフ）。

> **設計判断**：埋め込みではなく BM25 のため、overlap は小さめにして冗長コピーを抑える。recall@k 不足時に拡大する。

### 5.3 索引（indexer）

- ライブラリ：`bm25s`（高速、index dump 可）
- 種別ごとに別索引を作成（`code` と `docs` を分離 → ノイズ削減 + 質問種別に応じて重み付け可能）
- トークナイズ：lowercase + 単語境界 + 識別子の snake/camel 分解（コード検索の取りこぼし対策）
- 保存：`bm25s.dump` でディスクへ、チャンク本体は `chunks/*.jsonl`

### 5.4 性能予算

- vLLM ≒ 数千ファイル。AST 解析 + BM25 構築で 5 分以内に収めるため、`multiprocessing.Pool` で並列化（既定 `os.cpu_count()`）。
- 進捗は `tqdm` 表示。

---

## 6. Retrieval 設計

### 6.1 ロード

`Retriever` は索引と chunks を遅延ロード（CLI 引数で型を選択 or 両方検索して統合）。

### 6.2 検索フロー

```
query
  └─ tokenize（インデックスと同一前処理）
       └─ BM25 score（code / docs それぞれ）
            └─ 上位 N（既定 N=k*4）取得
                 └─ ファイルパス＋重なり領域でマージ／重複除去
                      └─ top-k を返す
```

- 出力は `MinimalSource` 配列（`file_path`, `first_character_index`, `last_character_index`）。
- 同一ファイル内の隣接チャンクは結合（隙間 < 100 文字なら統合）して recall@k 計算上の「重なり 5%」を取りやすくする。

### 6.3 質問種別

- 既定では code / docs 両方を検索しスコア正規化（min-max）してマージ。
- `--kind code|docs` で限定可能（`search_dataset` でデータセット種別に応じて切替）。

---

## 7. Generation 設計

### 7.1 LLM ロード

- `transformers.AutoModelForCausalLM` + `AutoTokenizer` で Qwen/Qwen3-0.6B。
- プロセス内シングルトンとしてキャッシュ。`bfloat16` + `device_map="auto"`。
- コールドスタート対策：`answer_dataset` 起動時に 1 度だけロード、後続は再利用。

### 7.2 プロンプト

```
System: あなたは vLLM コードベースに関する質問に答えるアシスタント。
        与えられた context のみを根拠に回答し、推測しない。
        簡潔で自己完結した日本語/英語の回答を出力する。
User:
  Context:
  --- source 1: <file_path>[<start>:<end>]
  <chunk text>
  --- source 2: ...
  Question: <question>
  Answer:
```

### 7.3 トークン制御

- 文脈は `max_context_length`（既定 2000 文字 ≒ ~600 トークン）でクリップ。
- top-k 順に詰め、上限を超えたら打ち切り。
- 生成は `max_new_tokens=256`, `do_sample=False`（決定的・自己完結性優先）。

### 7.4 出力

`MinimalAnswer` を組み立て `StudentSearchResultsAndAnswer` で保存。

---

## 8. Evaluation 設計

`evaluation/recall.py`：

```python
def overlap_ratio(a: MinimalSource, b: MinimalSource) -> float:
    if a.file_path != b.file_path: return 0.0
    inter = max(0, min(a.last, b.last) - max(a.first, b.first))
    union_len = b.last - b.first  # 正解側基準
    return inter / max(union_len, 1)

def recall_at_k(retrieved, gold, k, threshold=0.05) -> float:
    top = retrieved[:k]
    found = sum(any(overlap_ratio(r, g) >= threshold for r in top) for g in gold)
    return found / len(gold)
```

- `evaluate` コマンドは `Recall@1/3/5/10` を出力。
- 失敗質問のサンプルダンプ（任意の `--dump_failures` フラグ）でデバッグを容易化。

---

## 9. CLI 仕様（Fire）

`src/student/__main__.py` で `fire.Fire(CLI)`。

| コマンド | 引数 | 動作 |
| --- | --- | --- |
| `index` | `--raw_dir`, `--max_chunk_size=2000`, `--workers=auto` | 索引構築 |
| `search` | `query`, `--k=10`, `--kind=both` | 単一クエリ検索（標準出力 JSON） |
| `search_dataset` | `--dataset_path`, `--k=10`, `--save_directory`, `--kind=auto` | データセット一括検索 |
| `answer` | `query`, `--k=10` | 単一質問に回答 |
| `answer_dataset` | `--student_search_results_path`, `--save_directory` | 検索済結果に回答付与 |
| `evaluate` | `--student_answer_path`, `--dataset_path`, `--k=10` | recall@k 計算 |

- 全コマンドで `try/except` + ユーザー向けエラーメッセージ。
- 不正な引数（存在しないパス、空ファイル、k<=0 等）はクラッシュさせず終了コード 1。
- 長時間処理は `tqdm`。

---

## 10. 開発順序（実装ロードマップ）

> **原則**：subject ヒント通り「最も単純な方法で動かし、recall を測ってから磨く」。

1. **足場**: `pyproject.toml`（uv）、`Makefile`、`.gitignore`、`src/student/` 骨組み、pydantic モデル、空 CLI。
2. **Ingestion (v0)**: walker + TextChunker（段落分割のみ）+ PythonChunker（AST なしの単純行ベース）+ BM25 索引保存。
3. **Retrieval (v0)**: ロード・検索・top-k 返却。`search` CLI 動作確認。
4. **Evaluation**: `evaluate` を実装し AnsweredQuestions に対する recall@k をベースラインとして計測。
5. **Chunking 改善**: PythonChunker を AST ベースに、TextChunker を見出し境界対応に。再計測。
6. **Retrieval 改善**: トークナイザ調整（identifier 分解）、隣接チャンク統合、code/docs 重み調整。
7. **Generation**: Qwen3 ロード・プロンプト・`answer` / `answer_dataset`。
8. **仕上げ**: CLI エラーハンドリング、進捗バー、Makefile lint パス、README 執筆。
9. **ボーナス（任意）**: クエリ書換、ハイブリッド（BM25 + embeddings）、結果キャッシュ。

各段階で `make lint` と recall 計測をゲートにする。

---

## 11. 主要設計判断

| 論点 | 選択 | 理由 |
| --- | --- | --- |
| 取得手法 | BM25（bm25s） | コード+文書の語彙一致に強い、5分制約に収まる、埋め込みより軽い |
| 索引分離 | code / docs を別索引 | 質問種別に応じた重み付けが容易、ノイズ削減 |
| Python chunk | AST ベース | 関数単位の意味境界が recall を押し上げる |
| overlap | 小さめ（100–200） | BM25 では冗長性より語彙網羅の方が効く |
| LLM 起動 | シングルトンキャッシュ | コールドスタート 60 秒制約のため |
| 文脈長 | 2000 文字 × k | サブジェクト例に合わせる、Qwen3-0.6B のコンテキストに余裕 |

---

## 12. リスクと緩和策

| リスク | 緩和 |
| --- | --- |
| 索引付け 5 分超過 | 並列化、code/docs 分離、不要拡張子の除外 |
| recall@5 未達 | overlap 拡大、トークナイザの identifier 分解、隣接チャンク統合、ハイブリッド検索（ボーナス） |
| Qwen3 ロード遅延 | bf16 + device_map、初回ロード後プロセス常駐 |
| 不正データセット入力 | pydantic 検証 + try/except + 明示メッセージ |
| mypy/flake8 違反蓄積 | コミット毎に `make lint` |

---

## 13. テスト戦略（非提出）

- `tests/test_chunker.py`: AST 分割境界、長文の overlap、不正 Python フォールバック。
- `tests/test_recall.py`: overlap_ratio の境界（同一区間、部分重なり、別ファイル）。
- `tests/test_cli.py`: 各サブコマンドが空入力でクラッシュしないこと。
- 小型フィクスチャ（数ファイルの mini-vLLM）で end-to-end smoke test。

---

## 14. 次の一手

1. `pyproject.toml` と空のパッケージ骨格を作る。
2. `models.py` に pydantic モデルを実装してテストを通す。
3. v0 の ingestion + retrieval + evaluate を最短経路で実装し、ベースライン recall を計測する。

ここまで合意できれば、`pyproject.toml` と骨格の生成から着手します。
