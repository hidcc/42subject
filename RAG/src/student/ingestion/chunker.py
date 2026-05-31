import uuid
from .. import config
from ..models import Chunk


def chunk_text(text: str, file_path: str, kind: str,
               size: int = config.MAX_CHUNK_SIZE,
               overlap: int = config.OVERLAP) -> list[Chunk]:
    """1ファイル分の本文を、文字数ベースのスライディングウィンドウで刻む。
    """
    chunks: list[Chunk] = []
    if not text:
        return chunks

    step = max(1, size - overlap)
    for start in range(0, len(text), step):
        end = min(start + size, len(text))
        chunks.append(Chunk(
            chunk_id=str(uuid.uuid4()),
            file_path=file_path,
            first_character_index=start,
            last_character_index=end,
            text=text[start:end],
            kind=kind,
        ))
        if end == len(text):
            break
    return chunks
