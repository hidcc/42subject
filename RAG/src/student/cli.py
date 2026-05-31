from .ingestion.indexer import build_index
from .retrieval.retriever import search as retrieve


class CLI:
    def index(self, max_chunk_size: int = 2000) -> None:
        """vLLMのソースを刻んで bm25s 索引を作る。"""
        build_index()

    def search(self, query: str, kind: str = "docs", k: int = 10) -> None:
        """queryに対して kindの索引を引き、 ヒットした場所を画面に出す。"""
        sources = retrieve(query, kind, k)

        print(f'query: "{query}" (kind={kind}, k={k})')
        print(f"hits: {len(sources)}")
        for rank, s in enumerate(sources, start=1):
            print(
                f"{rank:>2}. {s.file_path} "
                f"[{s.first_character_index}:{s.last_character_index}]"
            )
