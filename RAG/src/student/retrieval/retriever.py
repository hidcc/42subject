"""BM25 索引をロードして検索する Retriever。"""

import bm25s

from .. import config
from ..models import Chunk, MinimalSource


class Retriever:
    """1 種別（code または docs）の索引を保持し、検索を提供する。"""

    def __init__(self, kind: str) -> None:
        """索引とチャンク本体を 1 度だけロードする。"""
        self.kind = kind
        self.bm25 = bm25s.BM25.load(str(config.INDEX_DIR / kind))
        self.chunks: list[Chunk] = []
        with open(config.CHUNKS_DIR / f"{kind}.jsonl") as f:
            for line in f:
                self.chunks.append(Chunk.model_validate_json(line))

    def search(self, query: str, k: int = 10) -> list[MinimalSource]:
        """クエリに対し上位 k チャンクを引き、Source 配列で返す。

        Args:
            query: 自然言語のクエリ文字列。
            k: 取得する最大件数。

        Returns:
            スコア降順の MinimalSource のリスト（最大 k 件）。
        """
        if not self.chunks or k <= 0:
            return []
        query_tokens = bm25s.tokenize(query, stopwords="en")
        results, scores = self.bm25.retrieve(query_tokens, k=min(k, len(self.chunks)))
        return [
            self.chunks[idx].to_source()
            for idx, score in zip(results[0], scores[0], strict=False)
            if score > 0  # マッチしたチャンクのみ（スコア0の無関係チャンクは除外）
        ]
