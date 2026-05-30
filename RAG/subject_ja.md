# RAG against the machine

## Will you answer my questions?

**Summary:** Retrieval Augmented Generation、それだけや。それがこのプロジェクトの目的やで。
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

**誕生日のパラドックス**っちゅうのは、確率論における古典的な問題で、確率がいかに直感に反するもんかを示しとる。事象の起こる確率がえらい低そうに見えても、機会が十分にあれば、わいらの直感が言うよりもずっと頻繁に発生するっちゅうことを示しとるんや。

問題はようこう提示されよる：

> **23人の生徒がおる教室で、少なくとも2人が同じ誕生日を共有する確率はいくらや？**

これはveridical paradox（真性逆理）—つまり一見間違うてるように見えるが実は正しい言明や。
答えは **50%**！ 驚きやろ？ 公式はこうや：

$$P(n) = 1 - \frac{365!}{(365-n)! \cdot 365^n}$$

ここで n は生徒の人数を表しとる。n = 23 のとき確率はおおよそ50%に達する。

もっとびっくりするんは、教室に70人おったら、少なくとも2人が同じ誕生日を共有する確率はおおよそ **99.9%** にまで上がるっちゅうこっちゃ。

「面白い豆知識やけど、このプロジェクトと何の関係があるんや？」と思うやろ。
暗号学の世界には、誕生日のパラドックスを利用してハッシュ関数の衝突を見つける攻撃が存在する。それが、ぴったりこう名付けられとる—**バースデー攻撃**（the birthday attack）や。

直感がいかにわいらを誤らせるか、そして数学がいかに総当たり的解法へ導いてくれるかを理解したところで、ほな、プロジェクトに進もか。

---

# Chapter II — AIに関する指示

## ● Context（文脈）

学習の旅において、AIは様々な作業を支援してくれる。AIツールの様々な機能と、それがどんな風にお主の作業を支えてくれるかをじっくり探ってみい。せやけど、常に慎重に向き合い、結果を批判的に評価せなアカン。コードであれ、ドキュメントであれ、アイデアであれ、技術的な説明であれ、お主の質問が適切に組み立てられたかどうか、生成された内容が正確かどうかは決して完全にはわからん。ピアの仲間は、過ちや盲点を避ける助けとなる貴重な資源や。

## ● 主なメッセージ

- AIを使うて反復的でしんどい作業を削減せい。
- プロンプティング技能を発達させい—コーディングと非コーディング両方—これは将来のお主のキャリアの糧となる。
- AIシステムの仕組みを学んで、よくあるリスク、バイアス、倫理的問題を予期して避けるんや。
- ピアと協力して技術的能力と人間的能力の両方を引き続き築き上げい。
- 完全に理解し責任を負える AI 生成内容のみ使え。

## ● 学習者の規則

- AIツールを探ってその仕組みを理解する時間を取れ。倫理的に使い、潜在的バイアスを減らせるよう。
- プロンプトを書く前に問題を熟考せい—これにより、より明確で詳細かつ的確な語彙を用いた関連性高いプロンプトが書ける。
- AI が生成したものは何でも、体系的にチェック・レビュー・質問・テストする習慣をつけえ。
- 常にピアレビューを求めい—自分の検証だけに頼るな。

## ● フェーズ成果

- 汎用および領域特化の両方のプロンプティング技能を発達させい。
- AIツールの効果的活用で生産性を向上させい。
- 計算的思考、問題解決、適応力、協調を強化し続けい。

## ● コメントと例

- 試験や評価など、本物の理解を示さなアカン状況にしょっちゅう出会うで。備えて、技術的・対人的両方の技能を築き続けい。
- ピアに自分の推論を説明し議論することで、理解の隙間が明らかになる。ピア学習を優先せい。
- AIツールはお主固有の文脈を欠き、一般的な回答を出しがちや。同じ環境を共有するピアの方が関連性高く正確な洞察を提供できる。
- AIは最ももっともらしい答えを生成する傾向があるが、ピアは別の視点や貴重なニュアンスを提供できる。品質チェックポイントとして頼れ。

### ✓ よい実践

「ソート関数のテスト方法どないする？」とAIに尋ねる。いくつか案をもろて、試してみる。ピアと結果をレビューし、共にアプローチを精錬する。

### ✗ 悪い実践

AIに関数全体を書かせ、プロジェクトに貼り付ける。ピア評価の時、何をしとるんか説明できん。信用を失い、プロジェクトに落ちる。

### ✓ よい実践

AIを使うてパーサを設計する。ピアと一緒にロジックをたどる。バグを二つ見つけ、共に書き直す—よりきれいで完全に理解されたもんに。

### ✗ 悪い実践

プロジェクトの重要部分のコードをCopilotに生成させる。コンパイルは通るが、パイプの扱いを説明できん。評価で正当化できず、プロジェクトに落ちる。

---

# Chapter III — 共通の指示

## III.1 一般規則

- プロジェクトは **Python 3.10 以降** で書かなアカン。
- **flake8** コーディング標準に準拠せなアカン。
- 関数は例外を優雅に処理し、クラッシュを避けねばならん。`try-except` ブロックを用いて潜在エラーを管理せい。ファイルや接続などのリソースには context manager を優先し、自動クリーンアップを保証せい。レビュー中に未処理例外でクラッシュしたら非機能とみなされる。
- すべてのリソース（ファイルハンドル、ネットワーク接続など）は漏洩を防ぐため適切に管理せなアカン。可能な所では context manager を使え。
- コードには関数パラメータ・返り値・変数の型ヒントを含めえ（`typing` モジュール使用）。`mypy` で静的型検査せい。すべての関数は `mypy` をエラー無しでパスせなあかん。
- 関数とクラスには PEP 257 に従う docstring を含めえ（Google または NumPy スタイル）—目的・パラメータ・返り値を文書化。

## III.2 Makefile

プロジェクトに `Makefile` を含めて共通タスクを自動化せい。次のルールを含む必要がある（必須の lint には指定フラグが含まれる。強化検査のため `--strict` を試すことを強く推奨）：

- **install**: `pip`, `uv`, `pipx` などお主の選ぶパッケージ管理ツールで依存をインストール
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

- プロジェクト機能を検証するテストプログラムを作れ（提出・採点はせん）。`pytest` や `unittest` などのフレームワークでエッジケースを網羅する単体テストを作れ。
- Python の生成物を除外する `.gitignore` を含めえ。
- 開発中の依存隔離のため仮想環境（`venv` や `conda`）の使用を推奨する。

*プロジェクト固有の追加要件があれば、この節の直下に直ちに述べられる。*

## III.4 概要（Overview）

新しいプロジェクトは新しい技術と新しい技能としばしば結びついとる。わいらは `call_me_maybe` で **function calling** を見たし、このプロジェクトでもAIの世界の探検を続けるんや。今回扱う主題は **RAG**。せやけど、RAG の中身を見る前に、それが何をするか焦点を当ててみよ。そのために一歩下がろか。

AIモデルを作る時、最初のステップの一つが訓練（training）や。モデルに**言語理解・推論・構造分析**といった技能を発達させたい。これを達成するために大量のデータを食わせる。訓練後、モデルは学んだことを「覚えとる」が、与えられたデータしか「知らん」。もっと新しい知識が欲しけりゃ再訓練が必要や—これはえらい時間がかかる過程や。

**訓練**は一つの *技術* や。**RAG** はもう一つの技術や。モデルにデータを直接食わすかわりに、RAGはモデルに外部情報源へのアクセスを与える—そしてその情報源は *お主の選択や*。
この二つの技術は組み合わせ可能や：モデルは依然として基礎を築くために前述の主要概念（言語理解、推論、構造分析）で訓練される必要があるが、知識については訓練データと外部接続とを組み合わせることができる。

## III.5 Retrieval Augmented Generation（RAG）とは何や？

現在地が分かったところで、RAGとは何か（まだ調べてへんなら）聞きたなるやろ？ 三つの主要概念に分解して理解しよ。

- **Indexing（索引付け）**: 取得の前にデータをインデックス化せなアカン。このステップは情報を構造化・整理し、後で検索可能にする。
- **Retrieving（取得）**: モデルはお主固有のデータでは訓練されとらんから、データベースを検索して最も有用な断片を *retrieve*（取得）する必要がある。まずモデルはお主の質問を理解せなアカン。それが済んだら、インデックス済みデータベースに対しクエリを照合して最良の結果を選び、最後に最も関連性高い情報を引き出す。これは **query encoding**、**similarity search**、**ranking** を含む。
- **Augmenting（拡張）**: AIが情報を取得したら、それを既に「知っとる」ものと組み合わせられる。せやけど、ほとんどの実用的応用では、モデルの内部知識よりも取得データに極力依存しようとする—両者を混ぜると古い情報や幻覚的回答につながる可能性があるから。取得結果から始めて、無関係な断片を除くため（潜在的 **noise** を避けるため）クリーン化・フィルタリングし、**context window** に挿入する。
- **Generating（生成）**: 情報を取得・拡張したら、AIがついに回答を生成できる！ テキスト書き、概念説明、コード片の生成、これがRAGの目に見える成果や。そのため、AIは **context window** を読み、当面の課題を理解し、知識を融合させ、出力を生成する。現代のRAGシステムは書きながら洗練し、表現を即時調整して一貫性を保ちクエリで要求された口調に合わせる。

すべてはっきりしたところで、前に進もか！

---

# Chapter IV — 共通の指示（プロジェクト固有）

## IV.1 一般規則

- このプロジェクトでは **Python 3.10** を使うこと。
- すべてのクラスは検証と型安全のため **pydantic** を使うこと。
- **flake8** コーディング標準に準拠すること。ボーナスファイルもこの標準の対象や。
- 関数は例外を優雅に処理せねばならん。try-except ブロックで潜在エラーを管理せい。レビュー中に未処理例外でクラッシュしたら非機能とみなされる。
- すべてのリソース（ファイルハンドル、DB接続など）は漏洩を防ぐため適切に管理せなアカン。

## IV.2 追加ガイドライン

- 好きなライブラリを使うてええ。**transformers, dspy, fire, tqdm, langchain, bm25s, chromadb** パッケージを強く推奨する。
- 以下のモデルを使うこと：
  - **Qwen/Qwen3-0.6B**（既定）
  - 他のモデルも使えるが **Qwen/Qwen3-0.6B** と動作すること
- プロジェクトおよびパッケージ管理には **uv** を使うこと。
- システムは Python Fire を用いた **CLI** を提供せねばならん。
- 長時間の処理には **tqdm** で進捗バーを実装すべし。

---

# Chapter V — 必須課題（Mandatory part）

## V.1 概要

このプロジェクトでは、コードベースに関する質問に答えられる **Retrieval-Augmented Generation (RAG) システム** を作る。具体的には：

1. **Ingest**（取り込み）：添付として提供される vLLM リポジトリを取り込み、検索可能な知識ベースを作る
2. **Search**（検索）：この知識ベースを検索して、与えられた質問に対する関連コード断片と文書を見つける
3. **Answer**（回答）：LLM（Qwen/Qwen3-0.6B）と取得した文脈を使うて質問に答える
4. **Evaluate**（評価）：recall@k メトリックを使うて取得システムの品質を評価する

お主のシステムは、vLLMプロジェクトに関する質問に対し関連するソースコード位置を正しく取得できるか、そして取得した文脈に基づいて正確な回答を生成できるかでテストされる。

## V.2 提供すべきもの

次を含む Python アプリケーションを作らなアカン：

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
- 明確なメッセージでエラーを優雅に処理せい。CLI 引数はエッジケースで徹底テストされる—堕落した入力でもクラッシュせず処理できるよう保証せい。

> ℹ️ **シンプルに始めえ！** 基本の TF-IDF または BM25 取得から始め、recall@k スコアを測れ。良いメトリックを持つ動作するベースラインができてから、もっと洗練された手法を試せ。

## V.3 中核機能

うんうん、わかっとるわかっとる。summary を丁寧に読んだお主は、もう **Retrieval-Augmented Generation (RAG)** をコーディングすることを理解しとる。

その文脈で実装すべき最小機能は：

- プロジェクトの添付ファイルからインデックス化された知識ベースを構築
- 最も関連性高い情報片を取得・ランク付け
- 文脈制約内で LLM に渡す
- 出力節で説明される構造化 JSON 出力を生成
- 各ファイルタイプ用のインテリジェントなチャンキング戦略を実装
- すべての操作に包括的な CLI を提供
- 評価メトリックと性能分析を含める

> ℹ️ **慌てるな！** 最も単純なアプローチで誤差を測ることから始めよ。誤差測定が改善されたら複雑な手法に進め。

## V.4 チャンキング戦略

プログラムは異なるファイルタイプに対し異なるチャンキング戦略を実装せなアカン：

- Python コードのチャンキング
- テキストのチャンキング

> 🗺️ **最大チャンクサイズは 2000 文字**、CLI 引数で設定可能にせなアカン。

## V.5 取得手法

次の二つの取得手法のうち一つを必ず実装せい、選択は任せる：

- TF-IDF
- BM25

他の取得手法も探検してええが、上記二つのうち一つは実装すること。

## V.6 RAG パイプライン

この節では mouli の完全なワークフローを raw ドキュメントから検索評価および回答生成まで記述する。

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

このコマンドはインデックス化済みドキュメントを用いて単一クエリに答えられるようにする。
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

### V.6.5 一つのデータセットを検索

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

型安全なデータ取り扱いのため、次の **pydantic** モデルを実装せなアカン。これらはデータ整合性を保証し、パイプライン全体で自動検証を提供する。

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

**提供されたモデルは土台や。** 実装に必要なら新しいモデルや追加フィールド（例：検索結果モデルに）を加えて拡張してええ。

## V.8 入力

**取り込みオプション：**

- **Repository**：リポジトリで有用と判断するファイルを全部インデックス化

各クエリに対し、システムはリポジトリの関連チャンクを取得し、出力と同じ形で証拠ベースの応答を生成せなアカン。

> ℹ️ 異なるチャンキング戦略に紐づいて、異なるファイルタイプ用に異なるインデックスを作ってもよい。

## V.9 出力

出力は提供される Pydantic モデルに準拠せねばならず、詳細な結果とメタデータを含む包括的な JSON ファイルでなければならん：

- **検索操作の場合**: `StudentSearchResults` モデルを用いる
  - `search_results`: `question_id` と `retrieved_sources` を含む `MinimalSearchResults` のリスト
  - `k`: 要求された結果数
- **回答生成の場合**: `StudentSearchResultsAndAnswer` モデルを用いる
  - `search_results`: `question_id`, `retrieved_sources`, `answer` を含む `MinimalAnswer` のリスト
  - `k`: 要求された結果数
- **ソース情報**: 各 `MinimalSource` には次を含む
  - `file_path`: ソースファイルへの完全パス
  - `first_character_index`: 開始文字位置
  - `last_character_index`: 終了文字位置

### 出力フォーマット

出力は提供されたモデルの最小基盤を守らねばならんが、次のように拡張できる：

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

ある質問の recall@k は、取得されたソースが正解ソースとどれだけ重なるかをチェックして計算される。あるソースは、取得ソースと任意の正解ソースの間に少なくとも 5% の重なりがあれば「**found**」とみなされる。質問に複数のソースがある場合、その質問に対する取得スコアは `number_found / total_number_of_correct_sources` や。

### VI.1.2 性能

システムは次に挙げる最小性能を満たさなアカン：

- **インデックス化時間**: 最大 5 分
- **コールドスタート遅延**: 最大 60 秒（システム起動後の最初の取得、モデルロード含む）
- **ウォーム取得スループット**: 1000 質問で最大 90 秒（コールドスタート後）
- **Recall@5**: docs 質問で 80%、code 質問で 50%

最小しきい値を超えると報酬が出る—より高い recall スコアは評価時に追加の単位を稼ぐ。

---

# Chapter VII — README 要件

`README.md` ファイルを Git リポジトリのルートに置かなアカン。その目的は、プロジェクトに不慣れな者（ピア、スタッフ、リクルーターなど）にプロジェクトの内容、実行方法、トピックに関する詳細情報の場所を素早く理解させること。

`README.md` には最低限以下を含めること：

- 最初の行は斜体で次のように書く：*This project has been created as part of the 42 curriculum by <login1>[, <login2>[, <login3>[...]]].*
- **Description** 節：プロジェクトの目的と概要を明確に提示
- **Instructions** 節：コンパイル・インストール・実行に関する情報を含む
- **Resources** 節：トピックに関する古典的参考資料（ドキュメント、記事、チュートリアル等）と、AIがどう使われたか（どんなタスク、プロジェクトのどの部分か）の説明
- 👉 **追加節がプロジェクトにより必要となることがある**（使用例、機能リスト、技術選択など）

*必要な追加事項は以下に明示される。*

このプロジェクトの場合、`README.md` には次も含めねばならん：

- **System architecture**：RAGパイプラインの構成要素と相互作用を記述
- **Chunking strategy**：文書分割のアプローチを説明
- **Retrieval method**：取得アルゴリズムとランキング機構を詳述
- **Performance analysis**：recall@k スコアとシステム性能を議論
- **Design decisions**：主要な実装選択を説明
- **Challenges faced**：直面した困難と解決策を文書化
- **Example usage**：システム実行の明確な例を提供

> ℹ️ READMEは **英語** で書かなアカン。

---

# Chapter VIII — ボーナス課題

ボーナス単位のために高度な RAG 機能を実装してええ。次のような領域があるが、これらに限らへん：

- クエリ拡張（例：同義語拡張、クエリ書き換え）
- 取得用の意味埋め込み（semantic embeddings）
- 結果キャッシング（インデックスキャッシング、クエリキャッシングなど）
- 複数手法を組み合わせるハイブリッド取得
- vLLM経由のローカルLLM推論

ボーナス機能は **README.md に記述するだけでなく、実装され動作せなアカン**。評価時に実演を求められることもある。

---

# Chapter IX — 提出とピア評価

通常通り Git リポジトリで課題を提出せい。防御中にはリポジトリ内の作業のみ評価される。ファイル名が正しいかしっかり再確認せえ。

リポジトリには次を含めねばならん：

- `src/` ディレクトリに実装
- 依存管理のための `pyproject.toml` と `uv.lock`
- 包括的な文書の `README.md`
- 解を動かすために必要な他の設定ファイル

> ⚠️ **大きなデータファイル、モデル重み、生成物をリポジトリに含めるな。** 評価者が評価過程で生成する。

## IX.1 Recode 指示

評価中、プロジェクトの **小規模な修正** が求められることがある。これは小さな振る舞いの変更、数行のコードの書き直し、または簡単に追加できる機能であろう。

このステップは**全プロジェクトに該当するとは限らん**が、評価ガイドラインに記載されとる場合は備えなアカン。

このステップは、プロジェクトの特定部分への実際の理解を検証するためのもんや。修正はお主の選ぶ開発環境（普段のセットアップ）で実行でき、特定の時間枠が評価の一部として定義されとらん限り、数分内に実行可能であるべき。

例えば、関数やスクリプトへの小さな更新、表示の修正、新情報を格納するためのデータ構造の調整などを求められる。

詳細（範囲、対象等）は **評価ガイドライン** に明記され、同じプロジェクトでも評価ごとに異なる場合がある。
