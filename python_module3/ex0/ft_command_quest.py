import sys

if __name__ == "__main__":
    args = sys.argv
    argc = len(args)
    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")
    if argc != 1:
        print(f"Arguments received: {argc - 1}")
        count = 1
        for arg in args[1:]:
            print(f"Argument {count}: {arg}")
            count += 1
    else:
        print("No arguments provided!")
    print(f"Total arguments: {argc}")
