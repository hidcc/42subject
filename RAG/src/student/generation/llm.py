"""Generation backends: transformers (Qwen3-0.6B, default) and Ollama."""

from __future__ import annotations

import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    PreTrainedModel,
    PreTrainedTokenizerBase,
)

from .ollama_llm import generate_ollama

MODEL_NAME = "Qwen/Qwen3-0.6B"

_model: PreTrainedModel | None = None
_tokenizer: PreTrainedTokenizerBase | None = None


def _device() -> str:
    "利用可能なアクセラレータ"
    if torch.cuda.is_available():
        return "cuda"
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def _load() -> tuple[PreTrainedModel, PreTrainedTokenizerBase]:
    """モデル/トークナイザを一度だけロードしてキャッシュ"""
    global _model, _tokenizer
    if _model is None or _tokenizer is None:
        _tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
        _model = model.to(_device())  # type: ignore[arg-type]
        _model.eval()
    return _model, _tokenizer


def _generate_transformers(system: str, user: str, max_new_tokens: int = 256) -> str:
    """transformers + Qwen3-0.6B で決定的に回答を生成する（既定）。"""
    model, tokenizer = _load()
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False,
    )
    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    with torch.no_grad():
        generated = model.generate(  # type: ignore[operator]
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id,
        )
    new_tokens = generated[0][inputs["input_ids"].shape[1] :]
    decoded = tokenizer.decode(new_tokens, skip_special_tokens=True)
    return decoded.strip()  # type: ignore[union-attr]


def generate(
    system: str,
    user: str,
    *,
    backend: str = "transformers",
    model: str = "qwen3:4b",
    ollama_host: str = "http://localhost:11434",
    max_new_tokens: int = 384,
) -> str:
    """backend に応じて生成を振り分ける（既定は transformers）。"""
    if backend == "ollama":
        return generate_ollama(system, user, model, ollama_host, max_new_tokens)
    return _generate_transformers(system, user, max_new_tokens)
