from typing import Literal

from pydantic import BaseModel


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


class StudentSearchResultsAndAnswer(BaseModel):
    search_results: list[MinimalAnswer]


class Chunk(BaseModel):
    chunk_id: str
    file_path: str
    first_character_index: int
    last_character_index: int
    text: str
    kind: Literal["code", "docs"]

    def to_source(self) -> MinimalSource:
        return MinimalSource(
            file_path=self.file_path,
            first_character_index=self.first_character_index,
            last_character_index=self.last_character_index,
        )
