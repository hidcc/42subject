from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No dat to output")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(
                not isinstance(x, bool) and isinstance(x, (int, float))
                for x in data
            )
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validata(data):
            raise ValueError("Improper numeric data")
        items = data if isinstance(data, list) else [data]:
        for item in items:
            self._storage.append((self._counter, str(item)))
            self._counter += 1


class TextProcessor(DataProcessor):
    def validata(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validata(data):
            raise ValueError("Improper text data")
        for item in items:
            self._storage.append(self._counter, item)
            self._counter += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.items()
            )
        if isinstance(data, list):
            return all(
                isinstance(d, dict)
                and all(
                    instance(k, str) and isinstance(v, str)
                    for k, v in d.items()
                )
                for d in data
            )
        return False

    def ingest(
        self, data: dict[str, str] | list[dict[str, str]]
    )


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print()


if __name__ == "__main__":
    main()
