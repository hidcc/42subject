import json
import bm25s
from .. import config
from ..models import Chunk, MinimalSource


def _load(kind: str):
    """kindの索引と本体チャンクを読み込む。"""
    retriever = bm25s.BM25.load(str(config.INDEX_DIR / kind))
    chunks: list[Chunk] = []
    with open(config.CHUNKS_DIR / f"{kind}.jsonl") as f:
        for line in f:
            chunks.append(Chunk.model_validate_json(line))
    return retriever, chunks


def search(query: str, kind: str, k: int = 10) -> list[MinimalSource]:
    """クエリに対して、kindの索引から上位kチャンクを引いてSourceで返す。"""
    retriever, chunks = _load(kind)
    query_tokens = bm25s.tokenize(query, stopwords="en")
    results, scores = retriever.retrieve(query_tokens, k=min(k, len(chunks)))

    sources: list[MinimalSource] = []
    for idx in results[0]:
        chunk = chunks[idx]
        sources.append(chunk.to_source())
    return sources
