"""Dense retrieval over a local Qdrant index using Ollama embeddings."""

from __future__ import annotations

from qdrant_client import QdrantClient

from .. import config
from ..models import MinimalSource
from .embeddings import embed


class DenseRetriever:
    """1 種別の Qdrant コレクションに対し dense 検索を行う。"""

    def __init__(
        self,
        kind: str,
        ollama_host: str = config.DEFAULT_OLLAMA_HOST,
        embed_model: str = config.EMBED_MODEL,
    ) -> None:
        """ローカル Qdrant クライアントを開く。"""
        self.kind = kind
        self.ollama_host = ollama_host
        self.embed_model = embed_model
        self.client = QdrantClient(path=str(config.QDRANT_DIR))

    def search(self, query: str, k: int = 10) -> list[MinimalSource]:
        """クエリを埋め込み、Qdrant で上位 k を引いて Source 配列で返す。"""
        if k <= 0:
            return []
        vector = embed([query], self.embed_model, self.ollama_host)[0]
        response = self.client.query_points(
            self.kind, query=vector, limit=k, with_payload=True
        )
        out: list[MinimalSource] = []
        for hit in response.points:
            payload = hit.payload or {}
            out.append(
                MinimalSource(
                    file_path=str(payload.get("file_path", "")),
                    first_character_index=int(payload.get("first", 0)),
                    last_character_index=int(payload.get("last", 0)),
                )
            )
        return out
