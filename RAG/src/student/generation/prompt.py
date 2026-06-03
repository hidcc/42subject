"""Prompt construction: re-read source spans and assemble context within a budget."""

from .. import config
from ..models import MinimalSource

SYSTEM_PROMPT = (
    "You answer questions about the vLLM codebase from retrieved context. "
    "The context snippets have ALREADY been selected as relevant: do NOT "
    "evaluate, summarize, or comment on them one by one, and do NOT explain "
    "your reasoning or process (never write 'Let me analyze...'). "
    "Respond with ONLY the final answer in 1-3 sentences, then a final line "
    "'Sources: <file paths>'. If the answer is not in the context, reply in "
    "one sentence that it is not covered."
)


def _read_span(source: MinimalSource) -> str:
    """ソースを実ファイルから読み直す。"""
    path = config.ROOT / source.file_path
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    return text[source.first_character_index : source.last_character_index]


def build_user_prompt(
    question: str,
    sources: list[MinimalSource],
    max_context_length: int = 4000,
) -> str:
    """retrieved_sources を連結しt user promptを作る。"""
    blocks: list[str] = []
    used = 0
    for i, source in enumerate(sources, start=1):
        if used >= max_context_length:
            break
        snippet = _read_span(source)[: max_context_length - used]
        if not snippet:
            continue
        used += len(snippet)
        blocks.append(f"[source {i}] {source.file_path}\n{snippet}")
    context = "\n\n".join(blocks) if blocks else "(no context retrieved)"
    return f"Context:\n{context}\n\nQuestion: {question}\n\nAnswer:"
