import os
from collections.abc import Iterator

from .. import config
from ..models import Kind


def iter_files() -> Iterator[tuple[str, Kind]]:
    """vLLMフォルダを再帰的に歩き、(file_path, kind)を1つずつ返すジェネレーター

    file_pathは"data/raw/vllm-0.10.1/..."の接頭辞付き相対パス
    kindは "code" or "docs"
    """
    for dirpath, dirnames, filenames in os.walk(config.RAW_DIR):
        dirnames[:] = [d for d in dirnames if d not in config.SKIP_DIRS]

        for name in filenames:
            ext = os.path.splitext(name)[1].lower()
            kind: Kind
            if ext in config.CODE_EXTS:
                kind = "code"
            elif ext in config.DOCS_EXTS:
                kind = "docs"
            else:
                continue

            abs_path = os.path.join(dirpath, name)
            rel = os.path.relpath(abs_path, config.ROOT)
            yield rel, kind
