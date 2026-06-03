"""Hybrid retrieval: fuse BM25 and dense rankings via weighted RRF.

On this vLLM corpus BM25 is the stronger signal (queries share exact technical
terms with the sources), so the fusion weights BM25 higher than dense. The
weights/rrf_k were tuned empirically against recall@5.
"""

from __future__ import annotations

from .. import config
from ..models import MinimalSource
from .dense_retriever import DenseRetriever
from .retriever import Retriever

_RRF_K = 10
_W_BM25 = 2.0
_W_DENSE = 1.0


def _key(source: MinimalSource) -> tuple[str, int, int]:
    return (
        source.file_path,
        source.first_character_index,
        source.last_character_index,
    )


class HybridRetriever:
    """BM25 と dense の順位を重み付き Reciprocal Rank Fusion で統合する。"""

    def __init__(
        self,
        kind: str,
        ollama_host: str = config.DEFAULT_OLLAMA_HOST,
        embed_model: str = config.EMBED_MODEL,
    ) -> None:
        """BM25 と dense の両 retriever を保持する。"""
        self.bm25 = Retriever(kind)
        self.dense = DenseRetriever(kind, ollama_host, embed_model)

    def search(self, query: str, k: int = 10, pool: int = 30) -> list[MinimalSource]:
        """各手法の上位 pool を重み付き RRF で融合し、top-k を返す。"""
        if k <= 0:
            return []
        weighted = [
            (self.bm25.search(query, pool), _W_BM25),
            (self.dense.search(query, pool), _W_DENSE),
        ]
        scores: dict[tuple[str, int, int], float] = {}
        sources: dict[tuple[str, int, int], MinimalSource] = {}
        for ranked, weight in weighted:
            for rank, source in enumerate(ranked):
                key = _key(source)
                scores[key] = scores.get(key, 0.0) + weight / (_RRF_K + rank)
                sources.setdefault(key, source)
        ordered = sorted(scores, key=lambda key: scores[key], reverse=True)
        return [sources[key] for key in ordered[:k]]
