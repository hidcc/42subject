"""Recall evaluation matching the moulinette"""

from ..models import (
    AnsweredQuestion,
    MinimalSource,
    RagDataset,
    StudentSearchResults,
)


def iou(s1: MinimalSource, s2: MinimalSource) -> float:
    """２範囲の IoU。 file_pathが違えば 0。"""
    if s1.file_path != s2.file_path:
        return 0.0
    inter = max(
        0,
        min(s1.last_character_index, s2.last_character_index)
        - max(s1.first_character_index, s2.first_character_index),
    )
    len1 = s1.last_character_index - s1.first_character_index
    len2 = s2.last_character_index - s2.first_character_index
    union = len1 + len2 - inter
    return inter / union if union > 0 else 0.0


def recall_for_question(
    retrieved: list[MinimalSource],
    gold: list[MinimalSource],
    k: int,
    threshold: float = 0.05,
) -> float:
    """1問の recall = (top-k で見つかった正解数) / (正解総数)。"""
    if not gold:
        return 0.0
    top = retrieved[:k]
    found = sum(1 for g in gold if any(iou(r, g) >= threshold for r in top))
    return found / len(gold)


def recall_at_k_on_dataset(
    student: StudentSearchResults,
    dataset: RagDataset,
    k_values: tuple[int, ...] = (1, 3, 5, 10),
    threshold: float = 0.05,
) -> tuple[dict[int, float], int]:
    """k ごとの平均 recall と、評価できた質問数を返す。"""
    gold_by_id: dict[str, list[MinimalSource]] = {
        q.question_id: q.sources for q in dataset.rag_questions if isinstance(q, AnsweredQuestion)
    }
    sums: dict[int, float] = {k: 0.0 for k in k_values}
    n = 0
    for res in student.search_results:
        gold = gold_by_id.get(res.question_id)
        if gold is None:
            continue
        n += 1
        for k in k_values:
            sums[k] += recall_for_question(res.retrieved_sources, gold, k, threshold)
    return ({k: (sums[k] / n if n else 0.0) for k in k_values}, n)
