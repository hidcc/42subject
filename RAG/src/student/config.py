from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

RAW_PREFIX = "data/raw/vllm-0.10.1"
RAW_DIR = ROOT / RAW_PREFIX

CODE_EXTS = {".py"}
DOCS_EXTS = {".md", ".rst", ".txt"}

PROCESSED_DIR = ROOT / "data" / "processed"
CHUNKS_DIR = PROCESSED_DIR / "chunks"
INDEX_DIR = PROCESSED_DIR / "bm25_index"
OUTPUT_DIR = ROOT / "data" / "output"

MAX_CHUNK_SIZE = 2000
OVERLAP = 200

SKIP_DIRS = {".git", "__pycache__", ".github",
             ".gemini", ".buildkite", "tests"}
KINDS = {"code", "docs"}
