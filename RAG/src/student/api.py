"""FastAPI app exposing the RAG pipeline over HTTP (bonus).

Endpoints: GET /health, GET /search, GET /answer. Retrieval method
(bm25/dense/hybrid) and generation backend (transformers/ollama) are query
params, mirroring the CLI. Launch with `python -m student serve` or
`uvicorn student.api:app`.

Security notes (this is the only untrusted-input surface):
- The Ollama host is read from the server-side ``OLLAMA_HOST`` env var, never
  from the request, to avoid SSRF.
- ``kind`` is validated against a strict character class to avoid path
  traversal when it is used to build index/chunk file paths.
"""

from __future__ import annotations

import os
import re

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .generation.llm import generate
from .generation.prompt import SYSTEM_PROMPT, build_user_prompt
from .models import MinimalSource
from .retrieval.dense_retriever import DenseRetriever
from .retrieval.hybrid_retriever import HybridRetriever
from .retrieval.retriever import Retriever

app = FastAPI(title="RAG against the machine", version="0.1.0")

# Ollama host is a server-side setting (not request-controlled) -> no SSRF.
_OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
_KIND_RE = re.compile(r"[A-Za-z0-9_-]{1,40}")


def _check_kind(kind: str) -> None:
    """`kind` を安全な文字種に限定（パストラバーサル防止）。"""
    if not _KIND_RE.fullmatch(kind):
        raise HTTPException(status_code=400, detail="invalid 'kind' parameter")


def _retrieve(query: str, kind: str, k: int, method: str) -> list[MinimalSource]:
    """method に応じて retriever を選び、上位 k の source を返す。"""
    if method == "dense":
        return DenseRetriever(kind, _OLLAMA_HOST).search(query, k)
    if method == "hybrid":
        return HybridRetriever(kind, _OLLAMA_HOST).search(query, k)
    return Retriever(kind).search(query, k)


class SearchResponse(BaseModel):
    query: str
    kind: str
    method: str
    k: int
    results: list[MinimalSource]


class AnswerResponse(BaseModel):
    query: str
    answer: str
    sources: list[MinimalSource]


@app.get("/health")
def health() -> dict[str, str]:
    """ヘルスチェック。"""
    return {"status": "ok"}


@app.get("/search")
def search(
    q: str,
    kind: str = "docs",
    k: int = 5,
    method: str = "bm25",
) -> SearchResponse:
    """検索結果（retrieved sources）を返す。"""
    _check_kind(kind)
    results = _retrieve(q, kind, k, method)
    return SearchResponse(query=q, kind=kind, method=method, k=k, results=results)


@app.get("/answer")
def answer(
    q: str,
    kind: str = "docs",
    k: int = 5,
    method: str = "bm25",
    backend: str = "transformers",
    model: str = "qwen3:4b",
    max_context_length: int = 4000,
) -> AnswerResponse:
    """検索＋生成した回答を返す。"""
    _check_kind(kind)
    sources = _retrieve(q, kind, k, method)
    user = build_user_prompt(q, sources, max_context_length)
    text = generate(
        SYSTEM_PROMPT, user, backend=backend, model=model, ollama_host=_OLLAMA_HOST
    )
    return AnswerResponse(query=q, answer=text, sources=sources)
