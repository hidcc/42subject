import sys
import typing


def file_parse(file: str) -> None:
    f: typing.IO = open(file, "r", encoding="utf-8")
    print("---")
    print()
    text = f.read()
    print(text)
    print()
    print("---")
    f.close()
    print(f"File '{file}' closed.")
    print()
    print("Transform data:")
    print("---")
    print()
    represent = "".join(line + "#\n" for line in text.splitlines())
    print(represent)
    print("---")
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    line = sys.stdin.readline()
    new_name = line.rstrip("\n")
    if new_name == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{new_name}'")
    try:
        out: typing.IO = open(new_name, "w", encoding="utf-8")
        out.write(represent)
        out.close()
        print(f"Data saved in file '{new_name}'.")
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{new_name}': {e}\n")
        sys.stderr.flush()
        print("Data not saved.")


def main() -> None:
    args = sys.argv
    if len(args) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{args[1]}'")
    try:
        file_parse(args[1])

    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{args[1]}': {e}\n")
        sys.stderr.flush()


if __name__ == "__main__":
    main()
