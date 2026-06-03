import ast
import uuid

from .. import config
from ..models import Chunk, Kind


def _line_starts(text: str) -> list[int]:
    """各行先頭の絶対文字オフセット表"""
    starts = [0]
    for line in text.splitlines(keepends=True):
        starts.append(starts[-1] + len(line))
    return starts


def _new_chunk(text: str, file_path: str, kind: Kind, a: int, b: int) -> Chunk:
    return Chunk(
        chunk_id=str(uuid.uuid4()),
        file_path=file_path,
        first_character_index=a,
        last_character_index=b,
        text=text[a:b],
        kind=kind,
    )


def _emit(
    text: str,
    file_path: str,
    kind: Kind,
    a: int,
    b: int,
    max_chunk_size: int,
    overlap: int = config.OVERLAP,
) -> list[Chunk]:
    """[a, b) を chunk化。max超ならスライディングウィンドウで分割。"""
    if b - a <= max_chunk_size:
        return [_new_chunk(text, file_path, kind, a, b)]
    chunks: list[Chunk] = []
    step = max(1, max_chunk_size - overlap)
    pos = a
    while pos < b:
        stop = min(pos + max_chunk_size, b)
        chunks.append(_new_chunk(text, file_path, kind, pos, stop))
        if stop == b:
            break
        pos += step
    return chunks


def _chunks_from_cuts(
    text: str,
    file_path: str,
    kind: Kind,
    cuts: list[int],
    max_chunk_size: int,
) -> list[Chunk]:
    """境界区間を max_chunk_size まで貪欲に結合しつつ、隙間なく chunk 化する。"""
    chunks: list[Chunk] = []
    ordered = sorted(set(cuts))
    pending: tuple[int, int] | None = None
    for a, b in zip(ordered, ordered[1:], strict=False):
        if b <= a:
            continue
        if b - a > max_chunk_size:
            if pending is not None:
                chunks.extend(_emit(text, file_path, kind, *pending, max_chunk_size))
                pending = None
            chunks.extend(_emit(text, file_path, kind, a, b, max_chunk_size))
            continue
        if pending is None:
            pending = (a, b)
        elif b - pending[0] <= max_chunk_size:
            pending = (pending[0], b)
        else:
            chunks.extend(_emit(text, file_path, kind, *pending, max_chunk_size))
            pending = (a, b)
    if pending is not None:
        chunks.extend(_emit(text, file_path, kind, *pending, max_chunk_size))
    return chunks


def split_python(text: str, file_path: str, max_chunk_size: int) -> list[Chunk]:
    """トップレベル def/class 境界で分割（全文カバー）。構文エラー時はテキスト分割。"""
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return split_text(text, file_path, max_chunk_size, kind="code")
    starts = _line_starts(text)
    cuts = [0, len(text)]
    for node in tree.body:
        line = node.lineno
        if (
            isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
            and node.decorator_list
        ):
            line = min(line, node.decorator_list[0].lineno)
        cuts.append(starts[line - 1])
    return _chunks_from_cuts(text, file_path, "code", cuts, max_chunk_size)


def split_text(
    text: str,
    file_path: str,
    max_chunk_size: int,
    kind: Kind = "docs",
) -> list[Chunk]:
    """Markdown 見出し(#) 境界で分割（全文カバー）。超過区間のみ窓分割。"""
    starts = _line_starts(text)
    cuts = [0, len(text)]
    for i, line in enumerate(text.splitlines(keepends=True)):
        if line.lstrip().startswith("#"):
            cuts.append(starts[i])
    return _chunks_from_cuts(text, file_path, kind, cuts, max_chunk_size)


def chunk_file(
    text: str,
    file_path: str,
    kind: Kind,
    max_chunk_size: int = config.MAX_CHUNK_SIZE,
) -> list[Chunk]:
    """種別に応じてチャンカを振り分ける（indexer はこれを呼ぶ）。"""
    if not text.strip():
        return []
    if kind == "code":
        return split_python(text, file_path, max_chunk_size)
    return split_text(text, file_path, max_chunk_size, kind=kind)
