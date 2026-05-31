import bm25s
from .. import config
from .walker import iter_files
from .chunker import chunk_text


def build_index() -> None:
    """全ファイルを刻んで、code/docs それぞれの索引と本体を保存する。"""
    config.CHUNKS_DIR.mkdir(parents=True, exist_ok=True)
    config.INDEX_DIR.mkdir(parents=True, exist_ok=True)

    buckets: dict[str, list] = {"code": [], "docs": []}
    for rel_path, kind in iter_files():
        abs_path = config.ROOT / rel_path
        text = abs_path.read_text(encoding="utf-8", errors="replace")
        buckets[kind].extend(chunk_text(text, rel_path, kind))

    for kind, chunks in buckets.items():
        with open(config.CHUNKS_DIR / f"{kind}.jsonl", "w") as f:
            for c in chunks:
                f.write(c.model_dump_json() + "\n")
        corpus = [c.text for c in chunks]
        tokens = bm25s.tokenize(corpus, stopwords="en")
        retriever = bm25s.BM25()
        retriever.index(tokens)
        retriever.save(str(config.INDEX_DIR / kind))

        print(f"[{kind}] files-chunks={len(chunks)} saved")
