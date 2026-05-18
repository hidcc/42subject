from typing import Any, Protocol
from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):
    name: str = "Data Processor"

    def __init__(self) -> None:
        self.storage: list[tuple[int, str]] = []
        self.counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.storage:
            raise IndexError("No data to output")
        return self.storage.pop(0)


class NumericProcessor(DataProcessor):
    name: str = "Numeric Processor"

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
            self.storage.append((self.counter, str(item)))
            self.counter += 1


class TextProcessor(DataProcessor):
    name: str = "Text Processor"

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
            self.storage.append((self.counter, item))
            self.counter += 1


class LogProcessor(DataProcessor):
    name: str = "Log Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            items = [data]
        elif isinstance(data, list):
            items = data
        else:
            return False
        for d in items:
            if not isinstance(d, dict):
                return False
            if 'log_level' not in d or 'log_message' not in d:
                return False
            if not all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in d.items()
            ):
                return False
        return True

    def ingest(
        self, data: dict[str, str] | list[dict[str, str]]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            text = f"{item['log_level']}: {item['log_message']}"
            self.storage.append((self.counter, text))
            self.counter += 1


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for elem in stream:
            for proc in self._processors:
                if proc.validate(elem):
                    proc.ingest(elem)
                    break
            else:
                print(
                    "DataStream error - "
                    f"Can't process element in stream: {elem}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            total = proc.counter
            remaining = len(proc.storage)
            print(
                f"{proc.name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            data: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    data.append(proc.output())
                except IndexError:
                    break
            plugin.process_output(data)


class CsvExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(value for _, value in data))


class JsonExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        parts = [f'"item_{rank}": "{value}"' for rank, value in data]
        print("{" + ", ".join(parts) + "}")


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print()
    print("Initialize Data Stream...")
    print()
    stream = DataStream()
    stream.print_processors_stats()
    print()

    print("Registering Processors")
    print()
    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(num)
    stream.register_processor(text)
    stream.register_processor(log)
    batch: list[typing.Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
             'log_message': 'User wil is connected'},
        ],
        42,
        ['Hi', 'five'],
    ]
    print(f"Send first batch of data on stream: {batch}")
    print()
    stream.process_stream(batch)
    stream.print_processors_stats()
    print()

    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CsvExportPlugin())
    print()
    stream.print_processors_stats()
    print()
    batch2: list[typing.Any] = [
        21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
         {'log_level': 'NOTICE', 'log_message':
         'Certificateexpires in 10 days'}],
        [32, 42, 64, 84, 128, 168], 'World hello']
    print(f"Send another batch of data: {batch2}")
    print()
    stream.process_stream(batch2)
    stream.print_processors_stats()
    print()
    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JsonExportPlugin())
    print()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
