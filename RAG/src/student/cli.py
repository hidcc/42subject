from pathlib import Path

from tqdm import tqdm

from .evaluation.recall import recall_at_k_on_dataset
from .generation.llm import generate
from .generation.prompt import SYSTEM_PROMPT, build_user_prompt
from .ingestion.embed_indexer import build_embeddings
from .ingestion.indexer import build_index
from .models import (
    MinimalAnswer,
    MinimalSearchResults,
    RagDataset,
    StudentSearchResults,
    StudentSearchResultsAndAnswer,
)
from .retrieval.dense_retriever import DenseRetriever
from .retrieval.hybrid_retriever import HybridRetriever
from .retrieval.retriever import Retriever


class CLI:
    def index(self, max_chunk_size: int = 2000) -> None:
        """vLLMのソースを刻んで bm25s 索引を作る。"""
        build_index(max_chunk_size=max_chunk_size)
        print("Ingestion complete! Indices saved under data/processed/")

    def index_embeddings(
        self,
        kind: str = "both",
        ollama_host: str = "http://localhost:11434",
        embed_model: str = "nomic-embed-text",
    ) -> None:
        """chunks を埋め込み、ローカル Qdrant に格納する（dense 検索の準備）。"""
        kinds = ["code", "docs"] if kind == "both" else [kind]
        for one in kinds:
            build_embeddings(one, ollama_host=ollama_host, embed_model=embed_model)

    def search(
        self,
        query: str,
        kind: str = "docs",
        k: int = 10,
        method: str = "bm25",
        ollama_host: str = "http://localhost:11434",
    ) -> None:
        """query を kind の索引で引き、ヒット位置を表示する（method=bm25|dense）。"""
        try:
            if method == "dense":
                sources = DenseRetriever(kind, ollama_host).search(query, k)
            elif method == "hybrid":
                sources = HybridRetriever(kind, ollama_host).search(query, k)
            else:
                sources = Retriever(kind).search(query, k)
        except FileNotFoundError:
            print("Index not found. Run 'index' (+ 'index_embeddings' for dense).")
            return

        print(f'query: "{query}" (kind={kind}, k={k}, method={method})')
        print(f"hits: {len(sources)}")
        for rank, s in enumerate(sources, start=1):
            print(f"{rank:>2}. {s.file_path} [{s.first_character_index}:{s.last_character_index}]")

    def search_dataset(
        self,
        dataset_path: str,
        k: int = 10,
        save_directory: str = "data/output/search_results",
        kind: str = "auto",
    ) -> None:
        """データセットの全質問を検索し、StudentSearchResults として保存する。"""
        path = Path(dataset_path)
        if not path.is_file():
            print(f"Dataset not found: {dataset_path}")
            return
        if k <= 0:
            print("k must be a positive integer.")
            return
        try:
            dataset = RagDataset.model_validate_json(path.read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"Failed to load dataset: {exc}")
            return

        if kind == "auto":
            kind = "code" if "code" in Path(dataset_path).name else "docs"
        retriever = Retriever(kind)

        results: list[MinimalSearchResults] = []
        for q in tqdm(dataset.rag_questions, desc=f"search[{kind}]"):
            sources = retriever.search(q.question, k)
            results.append(
                MinimalSearchResults(
                    question_id=q.question_id,
                    question_str=q.question,
                    retrieved_sources=sources,
                )
            )

        out = StudentSearchResults(search_results=results, k=k)
        save_dir = Path(save_directory)
        save_dir.mkdir(parents=True, exist_ok=True)
        out_path = save_dir / Path(dataset_path).name
        out_path.write_text(out.model_dump_json(indent=2))

        print(f"Saved student_search_results to {out_path}")

    def evaluate(
        self,
        student_answer_path: str,
        dataset_path: str,
        k: int = 10,
    ) -> None:
        """検索結果を正解データセットに対し recall@k で評価する。"""
        spath, dpath = Path(student_answer_path), Path(dataset_path)
        if not spath.is_file():
            print(f"Student results not found: {student_answer_path}")
            return
        if not dpath.is_file():
            print(f"Dataset not found: {dataset_path}")
            return
        try:
            student = StudentSearchResults.model_validate_json(spath.read_text(encoding="utf-8"))
            dataset = RagDataset.model_validate_json(dpath.read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"Failed to load inputs: {exc}")
            return

        k_values = tuple(sorted({1, 3, 5, 10, k}))
        scores, evaluated = recall_at_k_on_dataset(student, dataset, k_values)
        print("Evaluation Results")
        print("=" * 42)
        print(f"Questions evaluated: {evaluated}")
        for kk in k_values:
            print(f"Recall@{kk}: {scores[kk]:.3f}")

    def answer(
        self,
        query: str,
        k: int = 10,
        kind: str = "docs",
        max_context_length: int = 4000,
        backend: str = "transformers",
        ollama_host: str = "http://localhost:11434",
        model: str = "qwen3:4b",
    ) -> None:
        """単一質問を検索し、取得文脈で LLM に回答させる。"""
        try:
            sources = Retriever(kind).search(query, k)
        except FileNotFoundError:
            print("Index not found. Run 'index' first.")
            return
        user = build_user_prompt(query, sources, max_context_length)
        result = generate(
            SYSTEM_PROMPT, user,
            backend=backend, model=model, ollama_host=ollama_host,
        )
        label = model if backend == "ollama" else "Qwen3-0.6B"

        print(f"\nQuestion: {query}")
        print("=" * 60)
        print(f"Answer ({label}):")
        print("-" * 60)
        print(result)
        print("=" * 60)
        print("Sources used:")
        for i, s in enumerate(sources, start=1):
            print(
                f"  [{i}] {s.file_path} "
                f"[{s.first_character_index}:{s.last_character_index}]"
            )

    def answer_dataset(
        self,
        student_search_results_path: str,
        save_directory: str = "data/output/search_results_and_answer",
        max_context_length: int = 4000,
        backend: str = "transformers",
        ollama_host: str = "http://localhost:11434",
        model: str = "qwen3:4b",
    ) -> None:
        """検索結果(StudentSearchResults)に回答を付けて保存する。"""
        path = Path(student_search_results_path)
        if not path.is_file():
            print(f"Search results not found: {student_search_results_path}")
            return
        try:
            student = StudentSearchResults.model_validate_json(path.read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"Failed to load search results: {exc}")
            return
        answers: list[MinimalAnswer] = []
        for r in tqdm(student.search_results, desc="answer"):
            user = build_user_prompt(r.question_str, r.retrieved_sources, max_context_length)
            answers.append(
                MinimalAnswer(
                    question_id=r.question_id,
                    question_str=r.question_str,
                    retrieved_sources=r.retrieved_sources,
                    answer=generate(
                        SYSTEM_PROMPT, user,
                        backend=backend, model=model, ollama_host=ollama_host,
                    ),
                )
            )
        out = StudentSearchResultsAndAnswer(search_results=answers, k=student.k)
        save_dir = Path(save_directory)
        save_dir.mkdir(parents=True, exist_ok=True)
        out_path = save_dir / path.name
        out_path.write_text(out.model_dump_json(indent=2), encoding="utf-8")
        print(f"Saved student_search_results_and_answer to {out_path}")
