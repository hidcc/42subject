from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

RAW_PREFIX = "data/raw/vllm-0.10.1"
RAW_DIR = ROOT / RAW_PREFIX

CODE_EXTS = {".py"}
DOCS_EXTS = {".md", ".rst", ".txt"}
