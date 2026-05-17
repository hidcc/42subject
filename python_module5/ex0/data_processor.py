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
            raise IndexError("No data to output")
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
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append((self._counter, str(item)))
            self._counter += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append((self._counter, item))
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
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in d.items()
                )
                for d in data
            )
        return False

    def ingest(
        self, data: dict[str, str] | list[dict[str, str]]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            text = f"{item['log_level']}: {item['log_message']}"
            self._storage.append((self._counter, text))
            self._counter += 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print()
    print("Testing Numeric Processor...")
    num = NumericProcessor()
    print(f" Trying to validate input '42': {num.validate(42)}")
    print(f" Trying to validate input 'Hello': {num.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num.ingest("foo")
    except ValueError as e:
        print(f" Got exception: {e}")

    data_num: list[int | float] = [1, 2, 3, 4, 5]
    print(f" Processing data: {data_num}")
    num.ingest(data_num)
    print(" Extracting 3 values...")
    for _ in range(3):
        key, value = num.output()
        print(f" Numeric value {key}: {value}")
    print()

    print("Testing Text Processor...")
    text = TextProcessor()
    print(f" Trying to validate input '42': {text.validate(42)}")
    data_text = ["Hello", "Nexus", "World"]
    print(f" Processing data: {data_text}")
    text.ingest(data_text)
    print(" Extracting 1 value...")
    key, value = text.output()
    print(f" Text value {key}: {value}")
    print()

    print("Testing Log Processor...")
    log = LogProcessor()
    print(f" Trying to validate input 'Hello': {log.validate('Hello')}")
    data_log = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'}, {
        'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    print(f" Processing data: {data_log}")
    log.ingest(data_log)
    print(" Extracting 2 values...")
    for _ in range(2):
        key, value = log.output()
        print(f" Log entry {key}: {value}")


if __name__ == "__main__":
    main()
