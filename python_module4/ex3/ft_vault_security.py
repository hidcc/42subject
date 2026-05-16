def secure_archive(
    filename: str,
    action: str = "read",
    content: str = "",
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, mode="r", encoding="utf-8") as f:
                return (True, f.read())
        if action == "write":
            with open(filename, mode="w", encoding="utf-8") as f:
                f.write(content)
                return (True, "Content successfully written to file")
        return (False, f"Unknown action: '{action}'")
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    ok, data = secure_archive("ancient_fragment.txt")
    print((ok, data))
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "write", data))


if __name__ == "__main__":
    main()
