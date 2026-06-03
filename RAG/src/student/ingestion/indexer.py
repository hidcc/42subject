import bm25s

from .. import config
from ..models import Chunk, Kind
from .chunker import chunk_file
from .walker import iter_files


def build_index(max_chunk_size: int = config.MAX_CHUNK_SIZE) -> None:
    """全ファイルを刻んで、code/docs それぞれの索引と本体を保存する。"""
    config.CHUNKS_DIR.mkdir(parents=True, exist_ok=True)
    config.INDEX_DIR.mkdir(parents=True, exist_ok=True)

    buckets: dict[Kind, list[Chunk]] = {"code": [], "docs": []}
    for rel_path, kind in iter_files():
        abs_path = config.ROOT / rel_path
        text = abs_path.read_text(encoding="utf-8", errors="replace")
        buckets[kind].extend(chunk_file(text, rel_path, kind, max_chunk_size=max_chunk_size))

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


def build_pdf_index(
    pdf_path: str,
    name: str = "pdf",
    max_chunk_size: int = config.MAX_CHUNK_SIZE,
) -> None:
    """PDF を抽出・チャンク化し、kind=name の BM25 索引として保存する。"""
    from .pdf_loader import load_pdf_text

    text = load_pdf_text(pdf_path)
    chunks = chunk_file(text, pdf_path, "docs", max_chunk_size=max_chunk_size)
    if not chunks:
        print(f"[{name}] no text extracted from {pdf_path}")
        return
    config.CHUNKS_DIR.mkdir(parents=True, exist_ok=True)
    config.INDEX_DIR.mkdir(parents=True, exist_ok=True)
    with open(config.CHUNKS_DIR / f"{name}.jsonl", "w") as f:
        for c in chunks:
            f.write(c.model_dump_json() + "\n")
    tokens = bm25s.tokenize([c.text for c in chunks], stopwords="en")
    retriever = bm25s.BM25()
    retriever.index(tokens)
    retriever.save(str(config.INDEX_DIR / name))
    print(f"[{name}] indexed PDF: {len(chunks)} chunks from {pdf_path}")
