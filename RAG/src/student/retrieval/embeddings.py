"""Embeddings via Ollama (e.g. nomic-embed-text). Stdlib only."""

from __future__ import annotations

import json
import urllib.request

from .. import config


def embed(
    texts: list[str],
    model: str = config.EMBED_MODEL,
    host: str = config.DEFAULT_OLLAMA_HOST,
) -> list[list[float]]:
    """テキスト群を Ollama /api/embed で埋め込む（バッチ対応）。"""
    url = host.rstrip("/") + "/api/embed"
    body = json.dumps({"model": model, "input": texts}).encode("utf-8")
    req = urllib.request.Request(
        url, data=body, headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as exc:
        raise RuntimeError(f"Ollama embed failed ({url}): {exc}") from exc
    vectors = data.get("embeddings")
    if not isinstance(vectors, list):
        raise RuntimeError("Ollama embed: missing 'embeddings' in response")
    return [[float(x) for x in vec] for vec in vectors]
