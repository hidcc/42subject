"""Extract text from PDF files (bonus: diverse sources)."""

from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader


def load_pdf_text(path: str | Path) -> str:
    """PDF の全ページからテキストを抽出し、改行で連結して返す。"""
    reader = PdfReader(str(path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)
