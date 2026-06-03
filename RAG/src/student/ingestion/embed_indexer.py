"""Build a local Qdrant vector index from chunks using Ollama embeddings."""

from __future__ import annotations

from qdrant_client import QdrantClient, models
from tqdm import tqdm

from .. import config
from ..models import Chunk
from ..retrieval.embeddings import embed


def _load_chunks(kind: str) -> list[Chunk]:
    with open(config.CHUNKS_DIR / f"{kind}.jsonl") as f:
        return [Chunk.model_validate_json(line) for line in f]


def build_embeddings(
    kind: str,
    ollama_host: str = config.DEFAULT_OLLAMA_HOST,
    embed_model: str = config.EMBED_MODEL,
    batch_size: int = 64,
) -> None:
    """chunks/{kind}.jsonl を埋め込み、ローカル Qdrant コレクションに格納する。"""
    chunks = _load_chunks(kind)
    if not chunks:
        print(f"[{kind}] no chunks; run 'index' first.")
        return
    config.QDRANT_DIR.mkdir(parents=True, exist_ok=True)
    client = QdrantClient(path=str(config.QDRANT_DIR))
    try:
        dim = len(embed([chunks[0].text], embed_model, ollama_host)[0])
        if client.collection_exists(kind):
            client.delete_collection(kind)
        client.create_collection(
            kind,
            vectors_config=models.VectorParams(
                size=dim, distance=models.Distance.COSINE
            ),
        )
        for start in tqdm(range(0, len(chunks), batch_size), desc=f"embed[{kind}]"):
            batch = chunks[start : start + batch_size]
            vectors = embed([c.text for c in batch], embed_model, ollama_host)
            points = [
                models.PointStruct(
                    id=start + i,
                    vector=vec,
                    payload={
                        "file_path": c.file_path,
                        "first": c.first_character_index,
                        "last": c.last_character_index,
                    },
                )
                for i, (c, vec) in enumerate(zip(batch, vectors, strict=False))
            ]
            client.upsert(kind, points)
        print(f"[{kind}] embedded {len(chunks)} chunks -> Qdrant")
    finally:
        client.close()
