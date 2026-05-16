import sys
import typing


def file_parse(file: str) -> None:
    f: typing.IO[str] = open(file, "r", encoding="utf-8")
    print("---")
    print()
    text = f.read()
    print(text)
    print()
    print("---")
    f.close()
    print(f"File '{file}' closed.")


def main() -> None:
    args = sys.argv
    if len(args) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{args[1]}'")
    try:
        file_parse(args[1])

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{args[1]}': {e}")

    except OSError as e:
        print(f"Error opening file '{args[1]}': {e}")


if __name__ == "__main__":
    main()
