import uuid
from typing import Literal

from pydantic import BaseModel, Field

Kind = Literal["code", "docs"]


class MinimalSource(BaseModel):
    file_path: str
    first_character_index: int
    last_character_index: int


class MinimalSearchResults(BaseModel):
    question_id: str
    question_str: str
    retrieved_sources: list[MinimalSource]


class MinimalAnswer(MinimalSearchResults):
    answer: str


class StudentSearchResults(BaseModel):
    search_results: list[MinimalSearchResults]
    k: int


class StudentSearchResultsAndAnswer(StudentSearchResults):
    # 親の list[MinimalSearchResults] を list[MinimalAnswer] に絞る（subject 指定モデル）
    search_results: list[MinimalAnswer]  # type: ignore[assignment]


class Chunk(BaseModel):
    chunk_id: str
    file_path: str
    first_character_index: int
    last_character_index: int
    text: str
    kind: Kind

    def to_source(self) -> MinimalSource:
        return MinimalSource(
            file_path=self.file_path,
            first_character_index=self.first_character_index,
            last_character_index=self.last_character_index,
        )


class UnansweredQuestion(BaseModel):
    question_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    question: str


class AnsweredQuestion(UnansweredQuestion):
    sources: list[MinimalSource]
    answer: str


class RagDataset(BaseModel):
    rag_questions: list[AnsweredQuestion | UnansweredQuestion]
