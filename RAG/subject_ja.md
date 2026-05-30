# RAG against the machine

## Will you answer my questions?

**Summary:** Retrieval Augmented Generation、それだけ。それがこのプロジェクトの目的です。
**Made in collaboration with**
**Version:** 1.6

---

## 目次

- I. はじめに（Foreword）
- II. AIの使用に関する指示
- III. 共通の指示
- IV. 共通の指示（プロジェクト固有）
- V. 必須課題（Mandatory part）
- VI. 評価（Evaluation）
- VII. README要件
- VIII. ボーナス課題
- IX. 提出とピア評価

---

# Chapter I — はじめに（Foreword）

**誕生日のパラドックス**とは、確率論における古典的な問題で、確率がいかに直感に反するものかを示しています。ある事象の発生確率がきわめて低そうに見えても、機会が十分にあれば、直感が示すよりもずっと頻繁に発生するということを示します。

問題はよく次のように提示されます：

> **23人の生徒がいる教室で、少なくとも2人が同じ誕生日を共有する確率はいくらか？**

これは veridical paradox（真性逆理）—つまり一見間違っているように見えるが実は正しい言明です。
答えは **50%**！ 驚きですよね。式は次の通りです：

$$P(n) = 1 - \frac{365!}{(365-n)! \cdot 365^n}$$

ここで n は生徒の人数を表します。n = 23 のとき確率はおよそ50%に達します。

さらに驚くべきは、教室に70人いると、少なくとも2人が同じ誕生日を共有する確率がおよそ **99.9%** にまで上昇することです。

「面白い豆知識だが、このプロジェクトと何の関係があるのか？」と思うかもしれません。
暗号学の世界には、誕生日のパラドックスを利用してハッシュ関数の衝突を見つける攻撃が存在します。それはまさに **バースデー攻撃**（the birthday attack）と名付けられています。

直感がいかに我々を誤らせるか、そして数学がいかに総当たり的解法へ導くかを理解したところで、プロジェクトに進みましょう。

---

# Chapter II — AIに関する指示

## ● Context（文脈）

学習の旅において、AIはさまざまな作業を支援してくれます。AIツールのさまざまな機能と、それがどのように作業を支えてくれるかをじっくり探ってください。ただし、常に慎重に向き合い、結果を批判的に評価しなければなりません。コードであれ、ドキュメントであれ、アイデアであれ、技術的な説明であれ、自分の質問が適切に組み立てられたか、生成された内容が正確かどうかは決して完全には分かりません。ピアは、過ちや盲点を避ける助けとなる貴重なリソースです。

## ● 主なメッセージ

- AIを使って反復的・退屈な作業を削減すること。
- プロンプティング技能を発達させること—コーディングと非コーディング両方—これは将来のキャリアの糧となる。
- AIシステムの仕組みを学び、よくあるリスク、バイアス、倫理的問題を予期して避けること。
- ピアと協力して技術的能力と人間的能力の両方を引き続き築き上げること。
- 完全に理解し責任を負える AI 生成内容のみを使うこと。

## ● 学習者の規則

- AIツールを探ってその仕組みを理解する時間を取ること。倫理的に使用し、潜在的バイアスを減らせるように。
- プロンプトを書く前に問題を熟考すること—これにより、より明確で詳細かつ的確な語彙を用いた関連性の高いプロンプトが書ける。
- AI が生成したものは何でも、体系的にチェック・レビュー・質問・テストする習慣をつけること。
- 常にピアレビューを求めること—自分の検証だけに頼らない。

## ● フェーズ成果

- 汎用および領域特化の両方のプロンプティング技能を発達させる。
- AIツールの効果的活用で生産性を向上させる。
- 計算的思考、問題解決、適応力、協調を強化し続ける。

## ● コメントと例

- 試験や評価など、本物の理解を示さねばならない状況にしばしば出会う。備え、技術的・対人的両方の技能を築き続けること。
- ピアに自分の推論を説明し議論することで、理解の隙間が明らかになる。ピア学習を優先すること。
- AIツールは自分固有の文脈を欠き、一般的な回答を出しがち。同じ環境を共有するピアの方が関連性高く正確な洞察を提供できる。
- AIは最ももっともらしい答えを生成する傾向があるが、ピアは別の視点や貴重なニュアンスを提供できる。品質チェックポイントとして頼ること。

### ✓ よい実践

「ソート関数のテスト方法は？」とAIに尋ねる。いくつかアイデアをもらい、試してみる。ピアと結果をレビューし、共にアプローチを精錬する。

### ✗ 悪い実践

AIに関数全体を書かせ、プロジェクトに貼り付ける。ピア評価の時、何をしているか説明できない。信用を失い、プロジェクトに落ちる。

### ✓ よい実践

AIを使ってパーサーを設計する。ピアと一緒にロジックをたどる。バグを2つ見つけ、共に書き直す—よりきれいで完全に理解されたものに。

### ✗ 悪い実践

プロジェクトの重要部分のコードをCopilotに生成させる。コンパイルは通るが、パイプの扱いを説明できない。評価で正当化できず、プロジェクトに落ちる。

---

# Chapter III — 共通の指示

## III.1 一般規則

- プロジェクトは **Python 3.10 以降** で書かれなければならない。
- **flake8** コーディング標準に準拠すること。
- 関数は例外を優雅に処理し、クラッシュを避けること。`try-except` ブロックを用いて潜在的エラーを管理すること。ファイルや接続などのリソースには context manager を優先し、自動クリーンアップを保証すること。レビュー中に未処理例外でクラッシュした場合は非機能とみなされる。
- すべてのリソース（ファイルハンドル、ネットワーク接続など）はリークを防ぐため適切に管理すること。可能な所では context manager を使用すること。
- コードには関数パラメータ・戻り値・変数の型ヒントを含めること（`typing` モジュール使用）。`mypy` で静的型チェックを行うこと。すべての関数は `mypy` をエラー無しでパスしなければならない。
- 関数とクラスには PEP 257 に従う docstring を含めること（Google または NumPy スタイル）—目的・パラメータ・戻り値を文書化。

## III.2 Makefile

プロジェクトに `Makefile` を含め、共通タスクを自動化すること。次のルールを含む必要がある（必須の lint には指定フラグが含まれる。強化検査のため `--strict` を試すことを強く推奨）：

- **install**: `pip`, `uv`, `pipx` などの好みのパッケージ管理ツールで依存をインストール
- **run**: メインスクリプトを実行（例：Python インタプリタ経由）
- **debug**: Python 組み込みデバッガ（例：`pdb`）でメインスクリプトをデバッグモード実行
- **clean**: 一時ファイルやキャッシュ（`__pycache__`, `.mypy_cache` など）を削除
- **lint**: 以下を実行

```
flake8 .
mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
```

- **lint-strict**（任意）: `flake8 .` と `mypy . --strict` を実行

## III.3 追加ガイドライン

- プロジェクト機能を検証するテストプログラムを作成すること（提出・採点はしない）。`pytest` や `unittest` などのフレームワークでエッジケースを網羅する単体テストを作成すること。
- Python の生成物を除外する `.gitignore` を含めること。
- 開発中の依存隔離のため仮想環境（`venv` や `conda`）の使用を推奨する。

*プロジェクト固有の追加要件があれば、この節の直下に直ちに述べられる。*

## III.4 概要（Overview）

新しいプロジェクトはしばしば新しい技術と新しい技能と結びついています。`call_me_maybe` で **function calling** を見ましたが、このプロジェクトでもAIの世界の探検を続けます。今回扱う主題は **RAG** です。ただし、RAG の中身を見る前に、それが何をするかに焦点を当ててみましょう。そのために一歩下がります。

AIモデルを作る際、最初のステップの1つが訓練（training）です。モデルに **言語理解・推論・構造分析** といった技能を発達させたい。これを達成するために大量のデータを与えます。訓練後、モデルは学んだことを「覚えて」いますが、与えられたデータしか「知り」ません。より新しい知識が欲しければ再訓練が必要です—これはとても時間のかかる過程です。

**訓練**は1つの *技術* です。**RAG** はもう1つの技術です。モデルにデータを直接与える代わりに、RAGはモデルに外部情報源へのアクセスを与えます—そしてその情報源は *あなたの選択* です。
この2つの技術は組み合わせ可能です。モデルは依然として基礎を築くために前述の主要概念（言語理解、推論、構造分析）で訓練される必要がありますが、知識については訓練データと外部接続とを組み合わせることができます。

## III.5 Retrieval Augmented Generation（RAG）とは何か？

現在地が分かったところで、RAGとは何か（まだ調べていなければ）聞きたくなるでしょう。3つの主要概念に分解して理解しましょう。

- **Indexing（索引付け）**: 取得の前にデータをインデックス化しなければならない。このステップは情報を構造化・整理し、後で検索可能にする。
- **Retrieving（取得）**: モデルは特定のデータでは訓練されていないため、データベースを検索して最も有用な断片を *retrieve*（取得）する必要がある。まずモデルは質問を理解しなければならない。それが済んだら、インデックス済みデータベースに対しクエリを照合して最良の結果を選び、最後に最も関連性の高い情報を引き出す。これは **query encoding**、**similarity search**、**ranking** を含む。
- **Augmenting（拡張）**: AIが情報を取得したら、それをすでに「知って」いるものと組み合わせることができる。ただし、ほとんどの実用的応用では、モデルの内部知識よりも取得データに極力依存しようとする—両者を混ぜると古い情報や幻覚的回答につながる可能性があるため。取得結果から始めて、無関係な断片を除くため（潜在的 **noise** を避けるため）クリーニング・フィルタリングし、**context window** に挿入する。
- **Generating（生成）**: 情報を取得・拡張したら、AIはついに回答を生成できる！ テキストの作成、概念の説明、コード片の生成、これがRAGの目に見える成果である。そのため、AIは **context window** を読み、当面の課題を理解し、知識を融合させ、出力を生成する。現代のRAGシステムは書きながら洗練し、表現を即時調整して一貫性を保ち、クエリで要求された口調に合わせる。

すべて明確になったところで、前に進みましょう！

---

# Chapter IV — 共通の指示（プロジェクト固有）

## IV.1 一般規則

- このプロジェクトでは **Python 3.10** を使用すること。
- すべてのクラスは検証と型安全のため **pydantic** を使用すること。
- **flake8** コーディング標準に準拠すること。ボーナスファイルもこの標準の対象である。
- 関数は例外を優雅に処理しなければならない。try-except ブロックで潜在的エラーを管理すること。レビュー中に未処理例外でクラッシュした場合は非機能とみなされる。
- すべてのリソース（ファイルハンドル、DB接続など）はリークを防ぐため適切に管理すること。

## IV.2 追加ガイドライン

- 好みのライブラリを使用してよい。**transformers, dspy, fire, tqdm, langchain, bm25s, chromadb** パッケージを強く推奨する。
- 以下のモデルを使用すること：
  - **Qwen/Qwen3-0.6B**（既定）
  - 他のモデルも使用可能だが **Qwen/Qwen3-0.6B** と動作すること
- プロジェクトおよびパッケージ管理には **uv** を使用すること。
- システムは Python Fire を用いた **CLI** を提供しなければならない。
- 長時間の処理には **tqdm** で進捗バーを実装すべきである。

---

# Chapter V — 必須課題（Mandatory part）

## V.1 概要

このプロジェクトでは、コードベースに関する質問に答えられる **Retrieval-Augmented Generation (RAG) システム** を作ります。具体的には：

1. **Ingest**（取り込み）：添付として提供される vLLM リポジトリを取り込み、検索可能な知識ベースを作る
2. **Search**（検索）：この知識ベースを検索して、与えられた質問に対する関連コード断片と文書を見つける
3. **Answer**（回答）：LLM（Qwen/Qwen3-0.6B）と取得した文脈を使って質問に答える
4. **Evaluate**（評価）：recall@k メトリックを使って取得システムの品質を評価する

システムは、vLLMプロジェクトに関する質問に対し関連するソースコード位置を正しく取得できるか、そして取得した文脈に基づいて正確な回答を生成できるかでテストされます。

## V.2 提供すべきもの

次を含む Python アプリケーションを作成しなければならない：

### V.2.1 知識ベース取り込みシステム

- 添付の vLLM リポジトリの全ファイルを読み込み処理する
- Python コードと Markdown 文書のインテリジェントなチャンキングを実装
- TF-IDF または BM25 で検索可能な索引を作成
- 高速取得のため索引を保存（最大索引付け時間 5 分）

### V.2.2 取得システム

- インデックス化された知識ベース上で意味検索を実装
- 任意のクエリに対し top-k の最関連コード断片を返す
- 各結果には次を含めること：`file_path`, `first_character_index`, `last_character_index`
- JSON データセットからの複数質問のバッチ処理に対応
- docs 質問で少なくとも **recall@5 80%**、code 質問で **50%** を達成

### V.2.3 回答生成システム

- Qwen/Qwen3-0.6B モデルで自然言語の回答を生成
- 取得した文脈をトークン制限内で LLM に渡す
- 取得したコードと文書に基づいて回答を生成
- 提供される pydantic モデルに従う構造化 JSON を出力

良い回答は次の通り：

- **Self-contained（自己完結）**: 元の質問を見ずに読める
- **Source-grounded（根拠あり）**: 引用元を明示
- **Faithful（忠実）**: ソース内容に留まる（幻覚なし）
- **Relevant（関連）**: 質問に直接答える

### V.2.4 評価システム

- 取得品質を測るため recall@k メトリックを実装
- 取得ソースを正解アノテーションと比較
- 取得と正解ソースの重なりを計算（最低 5% 重なりで「見つかった」とカウント）
- 詳細な性能指標を提供

### V.2.5 コマンドラインインタフェース

- Python Fire で次のコマンドを持つ CLI を提供：
  - `index`: リポジトリをインデックス化
  - `search`: 単一クエリを検索
  - `search_dataset`: 複数質問を処理し検索結果を出力
  - `answer`: 単一質問に文脈付きで回答
  - `answer_dataset`: 検索結果から回答を生成
  - `evaluate`: 検索結果を正解に対し評価
- 長時間処理に進捗バーを含める
- 明確なメッセージでエラーを優雅に処理すること。CLI 引数はエッジケースで徹底的にテストされる—不正な入力でもクラッシュせず処理できるよう保証すること。

> ℹ️ **シンプルに始めよ！** 基本の TF-IDF または BM25 取得から始め、recall@k スコアを測定する。良いメトリックを持つ動作するベースラインができてから、より洗練された手法を試すこと。

## V.3 中核機能

すでに summary を丁寧に読んでいるので、**Retrieval-Augmented Generation (RAG)** をコーディングすることを理解しているはずです。

その文脈で実装すべき最小機能は：

- プロジェクトの添付ファイルからインデックス化された知識ベースを構築
- 最も関連性の高い情報片を取得・ランク付け
- 文脈制約内で LLM に渡す
- 出力節で説明される構造化 JSON 出力を生成
- 各ファイルタイプ用のインテリジェントなチャンキング戦略を実装
- すべての操作に包括的な CLI を提供
- 評価メトリックと性能分析を含める

> ℹ️ **慌てるな！** 最もシンプルなアプローチで誤差を測ることから始めよ。誤差測定が改善されてから、より複雑な手法に進むこと。

## V.4 チャンキング戦略

プログラムは異なるファイルタイプに対し異なるチャンキング戦略を実装しなければならない：

- Python コードのチャンキング
- テキストのチャンキング

> 🗺️ **最大チャンクサイズは 2000 文字** で、CLI 引数で設定可能にしなければならない。

## V.5 取得手法

次の2つの取得手法のうち1つを必ず実装すること、選択は自由：

- TF-IDF
- BM25

他の取得手法も探究してよいが、上記2つのうち1つは実装すること。

## V.6 RAG パイプライン

この節では mouli の完全なワークフローを raw ドキュメントから検索評価および回答生成まで記述します。

### V.6.1 事前ファイル

```
ls -l data/raw
total 11988
drwxr-xr-x 15 student student  4096 Aug 19 00:27 vllm-0.10.1
-rw-r--r--  1 student student 12267696 Nov  2 22:21 vllm-0.10.1.zip
```

### V.6.2 インデックス化

```
uv run python -m student index --max_chunk_size 2000
Ingestion complete! Indices saved under data/processed/
```

```
ls -l data/processed
total 8
drwxrwxr-x 4 student student 4096 Dec 9 10:09 bm25_index
drwxrwxr-x 3 student student 4096 Dec 9 10:09 chunks
```

### V.6.3 Answer: 文脈付きで単一クエリに答える

このコマンドはインデックス化済みドキュメントを用いて単一クエリに答えられるようにします。
Answer コマンド：

```
uv run python -m student answer "How to configure OpenAI server?" --k 10
```

*任意パラメータ：* `k` 取得する結果の数。

### V.6.4 データセットの表示

```
ls -lR data/datasets/
data/datasets/:
total 8
drwxr-xr-x 2 student student 4096 Dec 8 22:38 AnsweredQuestions
drwxr-xr-x 2 student student 4096 Dec 8 22:38 UnansweredQuestions

data/datasets/AnsweredQuestions:
total 132
-rw-rw-r-- 1 student student 65238 Dec 8 22:38 dataset_code_public.json
-rw-rw-r-- 1 student student 68817 Dec 8 22:38 dataset_docs_public.json

data/datasets/UnansweredQuestions:
total 40
-rw-rw-r-- 1 student student 19217 Dec 8 22:38 dataset_code_public.json
-rw-rw-r-- 1 student student 17525 Dec 8 22:38 dataset_docs_public.json
```

### V.6.5 1つのデータセットを検索

```
uv run python -m student search_dataset \
  --dataset_path data/datasets/UnansweredQuestions/dataset_docs_public.json \
  --k 10 \
  --save_directory data/output/search_results
Saved student_search_results to data/output/search_results/dataset_docs_public.json
```

```
ls -l data/output/search_results
total 4672
-rw-rw-r-- 1 student student 4780742 Dec 9 10:14 dataset_docs_public.json
```

### V.6.6 検索結果を評価

```
uv run python -m moulinette evaluate_student_search_results \
  --student_answer_path data/output/search_results/dataset_docs_public.json \
  --dataset_path data/datasets/AnsweredQuestions/dataset_docs_public.json \
  --k 10 \
  --max_context_length 2000
Student data is valid: True
Total number of questions: 100
Total number of questions with sources: 100
Total number of questions with student sources: 100

Evaluation Results
==========================================
Questions evaluated: 100
Recall@1: 0.450
Recall@3: 0.590
Recall@5: 0.650
Recall@10: 0.720
```

### V.6.7 データセットに回答

```
uv run python -m student answer_dataset \
  --student_search_results_path data/output/search_results/dataset_docs_public.json \
  --save_directory data/output/search_results_and_answer
Loaded 100 questions from data/output/search_results/dataset_docs_public.json
Processed 100 of 100 questions
Saved student_search_results_and_answer to data/output/search_results_and_answer/dataset_docs_public.json
```

```
ls -l data/output/search_results_and_answer
total 4688
-rw-rw-r-- 1 student student 4798366 Dec 9 10:23 dataset_docs_public.json
```

### V.6.8 回答を検査

```
i=42
jq -s --argjson i "$i" '
  . as [$docs, $results]
  | {
      index:    $i,
      question: $docs.rag_questions[$i].question,
      expected: $docs.rag_questions[$i].answer,
      predicted: $results.search_results[$i].answer
    }
' \
data/datasets/AnsweredQuestions/dataset_docs_public.json \
data/output/search_results_and_answer/dataset_docs_public.json

{
  "index": 42,
  "question": "What method needs to be overridden in BaseProcessingInfo to specify the maximum number of input items for each modality in vLLM multimodal models?",
  "expected": "You need to override the abstract method `get_supported_mm_limits` to return the maximum number of input items for each modality supported by the model. This method is part of the BaseProcessingInfo subclass used when contributing multimodal models to vLLM.",
  "predicted": "override the abstract method `get_supported_mm_limits` to return the maximum number of input items for each modality."
}
```

## V.7 データモデル

型安全なデータ取り扱いのため、次の **pydantic** モデルを実装しなければならない。これらはデータ整合性を保証し、パイプライン全体で自動検証を提供する。

**MinimalSource** モデルは最小の情報源を表す：

```python
class MinimalSource(BaseModel):
    file_path: str
    first_character_index: int
    last_character_index: int
```

**UnansweredQuestion** と **AnsweredQuestion** モデルは未回答と回答済みの質問を表す：

```python
class UnansweredQuestion(BaseModel):
    question_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    question: str

class AnsweredQuestion(UnansweredQuestion):
    sources: List[MinimalSource]
    answer: str
```

**RagDataset** モデルはRAG質問のデータセットを表す：

```python
class RagDataset(BaseModel):
    rag_questions: List[AnsweredQuestion | UnansweredQuestion]
```

**MinimalSearchResults** と **MinimalAnswer** モデルは検索結果と回答を表す：

```python
class MinimalSearchResults(BaseModel):
    question_id: str
    question: str
    retrieved_sources: List[MinimalSource]

class MinimalAnswer(MinimalSearchResults):
    answer: str
```

**StudentSearchResults** と **StudentSearchResultsAndAnswer** モデルは検索結果と回答付き検索結果を表す：

```python
class StudentSearchResults(BaseModel):
    search_results: List[MinimalSearchResults]
    k: int

class StudentSearchResultsAndAnswer(StudentSearchResults):
    search_results: List[MinimalAnswer]
```

**提供されたモデルは土台である。** 実装に必要なら新しいモデルや追加フィールド（例：検索結果モデルに）を加えて拡張してよい。

## V.8 入力

**取り込みオプション：**

- **Repository**：リポジトリで有用と判断するファイルをすべてインデックス化

各クエリに対し、システムはリポジトリの関連チャンクを取得し、出力と同じ形で証拠ベースの応答を生成しなければならない。

> ℹ️ 異なるチャンキング戦略に紐づいて、異なるファイルタイプ用に異なるインデックスを作成してよい。

## V.9 出力

出力は提供される Pydantic モデルに準拠しなければならず、詳細な結果とメタデータを含む包括的な JSON ファイルでなければならない：

- **検索操作の場合**: `StudentSearchResults` モデルを使用する
  - `search_results`: `question_id` と `retrieved_sources` を含む `MinimalSearchResults` のリスト
  - `k`: 要求された結果数
- **回答生成の場合**: `StudentSearchResultsAndAnswer` モデルを使用する
  - `search_results`: `question_id`, `retrieved_sources`, `answer` を含む `MinimalAnswer` のリスト
  - `k`: 要求された結果数
- **ソース情報**: 各 `MinimalSource` には次を含む
  - `file_path`: ソースファイルへの完全パス
  - `first_character_index`: 開始文字位置
  - `last_character_index`: 終了文字位置

### 出力フォーマット

出力は提供されたモデルの最小基盤を守らなければならないが、次のように拡張できる：

例：StudentSearchResults 出力

```json
"search_results": [
    {
        "question_id": "q1",
        "retrieved_sources": [
            {
                "file_path": "docs/serving/openai_compatible_server.md",
                "first_character_index": 9867,
                "last_character_index": 10100
            },
            {
                "file_path": "vllm/entrypoints/openai/api_server.py",
                "first_character_index": 267,
                "last_character_index": 400
            }
        ]
    }
],
"k": 10
```

回答については `StudentSearchResultsAndAnswer` モデルに従う：

例：StudentSearchResultsAndAnswer 出力

```json
"search_results": [
    {
        "question_id": "q1",
        "retrieved_sources": [
            {
                "file_path": "docs/serving/openai_compatible_server.md",
                "first_character_index": 9867,
                "last_character_index": 10100
            },
            {
                "file_path": "vllm/entrypoints/openai/api_server.py",
                "first_character_index": 267,
                "last_character_index": 400
            }
        ],
        "answer": "To configure the OpenAI compatible server in vLLM..."
    }
],
"k": 10
```

---

# Chapter VI — 評価

## VI.1 評価メトリック

プログラムの評価は、取得コンポーネントの有効性を測定する **recall@k** メトリックを用いて行われる。

### VI.1.1 Recall@k の計算

ある質問の recall@k は、取得されたソースが正解ソースとどれだけ重なるかをチェックして計算される。あるソースは、取得ソースと任意の正解ソースの間に少なくとも 5% の重なりがあれば「**found**」とみなされる。質問に複数のソースがある場合、その質問に対する取得スコアは `number_found / total_number_of_correct_sources` である。

### VI.1.2 性能

システムは次に挙げる最小性能を満たさなければならない：

- **インデックス化時間**: 最大 5 分
- **コールドスタート遅延**: 最大 60 秒（システム起動後の最初の取得、モデルロード含む）
- **ウォーム取得スループット**: 1000 質問で最大 90 秒（コールドスタート後）
- **Recall@5**: docs 質問で 80%、code 質問で 50%

最小しきい値を超えると報酬が与えられる—より高い recall スコアは評価時に追加の単位を稼ぐ。

---

# Chapter VII — README 要件

`README.md` ファイルを Git リポジトリのルートに置かなければならない。その目的は、プロジェクトに不慣れな者（ピア、スタッフ、リクルーターなど）にプロジェクトの内容、実行方法、トピックに関する詳細情報の場所を素早く理解させることである。

`README.md` には最低限以下を含めること：

- 最初の行は斜体で次のように書く：*This project has been created as part of the 42 curriculum by <login1>[, <login2>[, <login3>[...]]].*
- **Description** 節：プロジェクトの目的と概要を明確に提示
- **Instructions** 節：コンパイル・インストール・実行に関する情報を含む
- **Resources** 節：トピックに関する古典的参考資料（ドキュメント、記事、チュートリアル等）と、AIがどう使われたか（どのタスク、プロジェクトのどの部分か）の説明
- 👉 **追加節がプロジェクトにより必要となることがある**（使用例、機能リスト、技術選択など）

*必要な追加事項は以下に明示される。*

このプロジェクトの場合、`README.md` には次も含めなければならない：

- **System architecture**：RAGパイプラインの構成要素と相互作用を記述
- **Chunking strategy**：文書分割のアプローチを説明
- **Retrieval method**：取得アルゴリズムとランキング機構を詳述
- **Performance analysis**：recall@k スコアとシステム性能を議論
- **Design decisions**：主要な実装選択を説明
- **Challenges faced**：直面した困難と解決策を文書化
- **Example usage**：システム実行の明確な例を提供

> ℹ️ READMEは **英語** で書かなければならない。

---

# Chapter VIII — ボーナス課題

ボーナス単位のために高度な RAG 機能を実装してよい。次のような領域があるが、これらに限らない：

- クエリ拡張（例：同義語拡張、クエリ書き換え）
- 取得用の意味埋め込み（semantic embeddings）
- 結果キャッシング（インデックスキャッシング、クエリキャッシングなど）
- 複数手法を組み合わせるハイブリッド取得
- vLLM経由のローカルLLM推論

ボーナス機能は **README.md に記述するだけでなく、実装され動作しなければならない**。評価時に実演を求められることもある。

---

# Chapter IX — 提出とピア評価

通常通り Git リポジトリで課題を提出すること。防御中にはリポジトリ内の作業のみ評価される。ファイル名が正しいかしっかり再確認すること。

リポジトリには次を含めなければならない：

- `src/` ディレクトリに実装
- 依存管理のための `pyproject.toml` と `uv.lock`
- 包括的な文書の `README.md`
- 解を動かすために必要な他の設定ファイル

> ⚠️ **大きなデータファイル、モデル重み、生成物をリポジトリに含めないこと。** 評価者が評価過程で生成する。

## IX.1 Recode 指示

評価中、プロジェクトの **小規模な修正** が求められることがある。これは小さな振る舞いの変更、数行のコードの書き直し、または簡単に追加できる機能であろう。

このステップは **全プロジェクトに該当するとは限らない** が、評価ガイドラインに記載されている場合は備えなければならない。

このステップは、プロジェクトの特定部分への実際の理解を検証するためのものである。修正は好みの開発環境（普段のセットアップ）で実行でき、特定の時間枠が評価の一部として定義されていない限り、数分内に実行可能であるべきである。

例えば、関数やスクリプトへの小さな更新、表示の修正、新情報を格納するためのデータ構造の調整などを求められる。

詳細（範囲、対象等）は **評価ガイドライン** に明記され、同じプロジェクトでも評価ごとに異なる場合がある。
