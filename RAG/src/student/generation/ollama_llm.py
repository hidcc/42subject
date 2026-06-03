"""Ollama HTTP backend for generation (optional, on-prem GPU). Stdlib only."""

from __future__ import annotations

import json
import re
import urllib.request

_THINK = re.compile(r"<think>.*?</think>", re.DOTALL)


def _strip_think(text: str) -> str:
    """Qwen3 の <think>...</think> ブロックを除去する。"""
    return _THINK.sub("", text).strip()


def generate_ollama(
    system: str,
    user: str,
    model: str = "qwen3:4b",
    host: str = "http://localhost:11434",
    max_new_tokens: int = 256,
) -> str:
    """Ollama の /api/chat で決定的に回答を生成する。

    Args:
        system: システムプロンプト。
        user: 文脈＋質問を含む user メッセージ。
        model: Ollama のモデルタグ（例: qwen3:4b）。
        host: Ollama サーバの URL（既定 localhost、LAN なら http://<ip>:11434）。
        max_new_tokens: 生成する最大トークン数。

    Returns:
        think ブロックを除いた回答テキスト。
    """
    url = host.rstrip("/") + "/api/chat"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "stream": False,
        # think=True separates reasoning into message.thinking; message.content
        # is then the clean final answer. num_predict must fit reasoning+answer.
        "think": True,
        "options": {"temperature": 0, "num_predict": max(max_new_tokens, 4096)},
    }
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url, data=body, headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as exc:
        raise RuntimeError(f"Ollama request failed ({url}): {exc}") from exc
    content = str(data.get("message", {}).get("content", ""))
    return _strip_think(content)
