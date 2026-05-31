import os
from .. import config


def iter_files():
    """vLLMフォルダを再帰的に歩き、(file_path, kind)を1つずつ返すジェネレーター

    file_pathは"data/raw/vllm-0.10.1/..."の接頭辞付き相対パス
    kindは "code" or "docs"
    """
    for dirpatch, dirnames, filenames in os.walk(config.RAW_DIR):
        dirnames[:] = [d for d in dirnames if d not in config.SKIP_DIRS]

        for name in filenames:
            ext = os.path.splitext(name)[1].lower()
            if ext in config.CODE_EXTS:
                kind = "code"
            elif ext in config.DOCS_EXTS:
                kind = "docs"
            else:
                continue

            abs_path = os.path.join(dirpatch, name)
            rel = os.path.relpath(abs_path, config.ROOT)
            yield rel, kind
