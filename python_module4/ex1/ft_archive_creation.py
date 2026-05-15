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
    print()
    print("---")
    input_newfile = input("Enter new file name (or empty): ")
    if len(input_newfile) < 1:
        print("Not saving data.")
        return
    print(f"Saving data to '{input_newfile}'")
    out: typing.IO = open(input_newfile, "w", encoding="utf-8")
    out.write(represent)
    out.close()
    print(f"Data saved in file '{input_newfile}'.")


def main() -> None:
    args = sys.argv
    if len(args) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{args[1]}'")
    try:
        file_parse(args[1])

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{args[1]}': {e}")

    except OSError as e:
        print(f"Error opening file '{args[1]}': {e}")


if __name__ == "__main__":
    main()
