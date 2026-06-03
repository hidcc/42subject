*This project has been created as part of the 42 curriculum by hakuta.*


# RAG against the machine

A Retrieval-Augmented Generation (RAG) system that answers questions about the
**vLLM** codebase. It ingests the repository into a searchable index, retrieves
the most relevant source/documentation spans for a question, and generates a
grounded answer with **Qwen/Qwen3-0.6B**.

## Description

The goal is to answer natural-language questions about a codebase by combining
**lexical retrieval** (BM25) with a small local **LLM**. Given a question, the
system returns the top-k most relevant source locations
(`file_path`, `first_character_index`, `last_character_index`) and an
evidence-based answer that cites those sources. Retrieval quality is measured
with **recall@k** against ground-truth annotations.

## System architecture

The pipeline is split into four decoupled layers under `src/student/`:

```
                          CLI (Python Fire)  — src/student/cli.py
   index │ search │ search_dataset │ answer │ answer_dataset │ evaluate
        │                  │                     │                 │
   ┌────▼─────┐      ┌─────▼──────┐        ┌─────▼──────┐    ┌─────▼──────┐
   │ Ingestion│      │ Retrieval  │        │ Generation │    │ Evaluation │
   │ walker   │      │ BM25 load  │        │ Qwen3-0.6B │    │ recall@k   │
   │ chunker  │      │ top-k      │        │ prompt     │    │ (IoU≥0.05) │
   │ indexer  │      └────────────┘        └────────────┘    └────────────┘
   └────┬─────┘
        ▼
   data/processed/  (chunks/*.jsonl  +  bm25_index/{code,docs})
```

- **Ingestion** (`ingestion/`): `walker` enumerates and classifies files,
  `chunker` splits them into chunks (per file type), `indexer` builds and
  persists one BM25 index per kind.
- **Retrieval** (`retrieval/retriever.py`): loads an index + its chunks and
  returns the top-k `MinimalSource` for a query.
- **Generation** (`generation/`): `prompt` rebuilds context from the retrieved
  spans, `llm` runs Qwen3-0.6B (loaded once, process-singleton).
- **Evaluation** (`evaluation/recall.py`): recall@k using the same IoU-based
  overlap rule as the grader.
- **Models** (`models.py`): pydantic models for type-safe I/O.

## Chunking strategy

Different file types use different strategies, with a shared core that
guarantees **full-file coverage** and **exact character offsets**:

- **Python (`.py`)** — boundaries are taken at top-level `def`/`class` nodes via
  the `ast` module (decorators included). On `SyntaxError` it falls back to the
  text strategy.
- **Text / Markdown (`.md`, `.rst`, `.txt`)** — boundaries are taken at Markdown
  headings (`#`).
- **Packing** — adjacent boundary segments are greedily merged up to
  `max_chunk_size` (default **2000**, configurable via `--max_chunk_size`).
  Segments larger than the limit are split with a sliding window (overlap 200).

Offsets are computed from a per-line start table, so every chunk satisfies
`file_text[first:last] == chunk_text` (verified: 0 mismatches on a 200-chunk
sample per kind).

## Retrieval method

- **Algorithm**: **BM25** (via the `bm25s` library), chosen over dense
  embeddings for strong lexical matching on code/identifiers and fast,
  dependency-light indexing.
- **Separate indices** for `code` and `docs` reduce cross-domain noise and let
  `search_dataset` pick the index by dataset type.
- **Ranking**: queries are tokenized with the same preprocessing as the corpus
  (lowercasing + English stopword removal); BM25 scores rank chunks and the
  top-k are returned as `MinimalSource`.

## Performance analysis

Measured on the public `AnsweredQuestions` datasets (100 questions each), using
the grader's overlap rule (`IoU ≥ 0.05`):

| Dataset | Recall@1 | Recall@3 | Recall@5 | Recall@10 | Target @5 |
|---------|---------:|---------:|---------:|----------:|:---------:|
| docs    | 0.660    | 0.850    | **0.880** | 0.930    | ≥ 0.80 ✓ |
| code    | 0.390    | 0.540    | **0.600** | 0.630    | ≥ 0.50 ✓ |

- **Indexing**: ~9,552 code chunks + ~790 docs chunks, well within the 5-minute
  budget. (Run `time make index` to measure on your machine.)
- **Cold start**: Qwen3-0.6B loads from cache in a few seconds (< 60s).
- **Warm retrieval**: BM25 retrieval is sub-second per query, comfortably within
  the 1000-questions / 90-second budget.

> Note on chunk granularity: pure one-node-per-chunk AST splitting dropped code
> recall@5 to ~0.50 (too fine-grained); **packing** segments back up to
> `max_chunk_size` raised it to ~0.60 while keeping semantic boundaries.

### Retrieval methods compared (bonus)

I added dense retrieval (Ollama `nomic-embed-text` + a local Qdrant vector DB)
and a weighted Reciprocal Rank Fusion hybrid, then measured all three:

| Method                | docs Recall@5 | code Recall@5 |
|-----------------------|--------------:|--------------:|
| BM25 (default)        | **0.880**     | **0.600**     |
| Dense (nomic-embed)   | 0.610         | 0.290         |
| Hybrid (weighted RRF) | 0.880         | 0.590         |

**Finding:** lexical BM25 wins on this corpus because the questions share exact
technical vocabulary (flags, class names, endpoints) with the sources. A
general-purpose embedding model underperforms, and the hybrid only matches BM25
once dense is down-weighted. **Decision:** keep BM25 as the default; dense and
hybrid are available as options (`search --method dense|hybrid`). Making dense
competitive would need a code/domain-tuned embedding model and finer chunks — a
clear next step.

**Worked example** — query *"How do I enable prefix caching in vLLM?"*, top results:

| Method | Top source(s) |
|--------|---------------|
| BM25   | `benchmarks/README.md` — the doc that carries the literal `--enable-prefix-caching` flag |
| Dense  | `docs/features/automatic_prefix_caching.md`, `docs/design/prefix_caching.md` — the concept/design docs |
| Hybrid | `automatic_prefix_caching.md` + `benchmarks/README.md` — keeps both the feature doc and the runnable-flag doc |

BM25 matches the literal flag, dense matches the concept, and the hybrid fuses
both. The Ollama (`qwen3:4b`) answer for this query:

> To enable prefix caching in vLLM, use the `--enable-prefix-caching` flag … which
> caches the KV cache of existing queries to reuse for queries sharing the same
> prefix. *(Sources: benchmarks/README.md)*

## Design decisions

- **BM25 over embeddings** — lighter, fast to build, strong on exact code tokens.
- **Two indices (code/docs)** — domain separation improves precision.
- **AST + packing** — semantic boundaries without over-fragmentation.
- **Singleton LLM** — load once to honor the cold-start budget and reuse across
  `answer_dataset`.
- **`enable_thinking=False`** — suppresses Qwen3's `<think>` blocks so answers
  are self-contained.
- **`question_str` field** — matches the grader's schema (the subject PDF shows
  `question`, but the moulinette validates `question_str`).
- **BM25 over dense — validated, not assumed** — measured BM25 vs dense vs hybrid
  and kept BM25 as the default based on the data (see comparison above).
- **On-prem extensions** — an optional Ollama generation backend
  (`--backend ollama`) and a Qdrant vector DB mirror a production RAG stack; the
  default path uses neither and runs anywhere.

## Instructions

Requirements: **Python 3.10**, [`uv`](https://docs.astral.sh/uv/). The vLLM
repository and the datasets are provided by the evaluator under `data/`.

```bash
make install        # uv sync --extra dev
make run            # show the CLI usage
make lint           # flake8 . + mypy . (project flags)
make lint-strict    # flake8 . + mypy . --strict
make clean          # remove generated indices/outputs and caches
```

## Example usage

```bash
# 1) Build the index (max chunk size configurable)
uv run python -m student index --max_chunk_size 2000

# 2) Search a single query
uv run python -m student search "How to load a LoRA adapter?" --kind docs --k 5

# 3) Batch search a dataset -> StudentSearchResults JSON
uv run python -m student search_dataset \
  --dataset_path data/datasets/UnansweredQuestions/dataset_docs_public.json \
  --k 10 --save_directory data/output/search_results

# 4) Evaluate retrieval quality (recall@k)
uv run python -m student evaluate \
  --student_answer_path data/output/search_results/dataset_docs_public.json \
  --dataset_path data/datasets/AnsweredQuestions/dataset_docs_public.json --k 10

# 5) Answer a single question with retrieved context
uv run python -m student answer "How to configure OpenAI server?" --k 5

# 6) Generate answers for a whole search-results file
uv run python -m student answer_dataset \
  --student_search_results_path data/output/search_results/dataset_docs_public.json \
  --save_directory data/output/search_results_and_answer
```

### Verified example questions for `answer`

The following documentation questions reliably retrieve the right context
(rank-1) and produce grounded, faithful answers from Qwen3-0.6B:

```bash
uv run python -m student answer "How do I start the vLLM OpenAI-compatible server?" --kind docs --k 5
# -> vllm serve <model>

uv run python -m student answer "Which quantization methods does vLLM support?" --kind docs --k 5
# -> AWQ (x86), GPTQ (x86), compressed-tensor INT8 W8A8

uv run python -m student answer "Which Python environment manager does vLLM recommend for installation?" --kind docs --k 5
# -> uv

uv run python -m student answer "How do I run offline batched inference with the vLLM LLM class?" --kind docs --k 5
# -> pip install vllm, then use the LLM class (see examples/offline_inference/basic/basic.py)

uv run python -m student answer "How do I enable prefix caching in vLLM?" --kind docs --k 5
# -> --enable-prefix-caching

uv run python -m student answer "How do I set the tensor parallel size in vLLM?" --kind docs --k 5
# -> --tensor-parallel-size N (with a vllm serve example)

uv run python -m student answer "What environment variable selects the attention backend in vLLM?" --kind docs --k 5
# -> VLLM_ATTENTION_BACKEND
```

Tip: ask single-intent questions using vLLM-specific terms. Vague queries
(e.g. "How to use OpenAI?") retrieve scattered context and yield weaker answers.

### Bonus extensions usage

These optional features sit on top of the core BM25 pipeline. **The mandatory
commands (`index`, `search`, `search_dataset`, `evaluate`, `answer`,
`answer_dataset`) need no Ollama and no GPU.** Install the extras only to use the
bonus features:

```bash
uv sync --extra bonus    # adds qdrant-client, fastapi, uvicorn, pypdf
```

What needs Ollama, and what does not:

| Command | Needs Ollama? |
|---------|:-------------:|
| `index`, `search` (bm25), `search_dataset`, `evaluate` | no |
| `answer` (default `transformers` / Qwen3-0.6B), `index_pdf` | no |
| `answer --backend ollama` | yes — generation |
| `index_embeddings`, `search --method dense\|hybrid` | yes — embeddings |

**On-prem / local generation via Ollama** (richer answers from a larger model):

```bash
# Requires: ollama pull qwen3:4b   (a local Ollama defaults to localhost:11434)
uv run python -m student answer "How do I enable prefix caching in vLLM?" \
  --backend ollama --model qwen3:4b --k 5
# for an Ollama server on another machine: add --ollama_host http://<host>:11434
```

**Dense / hybrid retrieval** (Ollama `nomic-embed-text` + a local Qdrant DB):

```bash
# Requires: ollama pull nomic-embed-text
uv run python -m student index_embeddings --kind both       # build the vector index once
uv run python -m student search "How do I dynamically load a LoRA adapter?" \
  --kind docs --method dense --k 5                          # or: --method hybrid
```

**HTTP API (FastAPI)** — exposes the pipeline over REST, with a Swagger UI at `/docs`:

```bash
# The Ollama host is read from OLLAMA_HOST (server-side, not the request) to avoid SSRF.
OLLAMA_HOST=http://<host>:11434 make serve     # = uvicorn student.api:app on :8000
# then, from another terminal or the browser:
curl "http://127.0.0.1:8000/health"
curl "http://127.0.0.1:8000/search?q=prefix+caching&kind=docs&method=hybrid&k=3"
curl "http://127.0.0.1:8000/answer?q=How+to+enable+prefix+caching&backend=ollama"
# interactive UI: http://127.0.0.1:8000/docs
```

**PDF ingestion** (diverse sources) — works with no Ollama (default backend):

```bash
# Extract + index any PDF under a label, then query it via --kind <label>
uv run python -m student index_pdf --pdf_path "path/to/doc.pdf" --name mydoc
uv run python -m student search "..." --kind mydoc --k 3
uv run python -m student answer "..." --kind mydoc --k 5    # default Qwen3-0.6B, no Ollama
```

## Resources

- BM25 / Okapi BM25 — ranking function for lexical retrieval.
- `bm25s` — fast BM25 implementation used here.
- vLLM — the codebase being indexed (`https://github.com/vllm-project/vllm`).
- Qwen3 — `Qwen/Qwen3-0.6B` (Hugging Face `transformers`).
- Retrieval-Augmented Generation (Lewis et al., 2020).
