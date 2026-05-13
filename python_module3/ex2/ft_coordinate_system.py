import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        s = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = s.split(',')
        try:
            a, b, c = parts
        except ValueError:
            print("Invalid syntax")
            continue

        a = a.strip()
        try:
            x = float(a)
        except ValueError as e:
            print(f"Error on parameter '{a}': {e}")
            continue

        b = b.strip()
        try:
            y = float(b)
        except ValueError as e:
            print(f"Error on parameter '{b}': {e}")
            continue

        c = c.strip()
        try:
            z = float(c)
        except ValueError as e:
            print(f"Error on parameter '{c}': {e}")
            continue

        return (x, y, z)


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    p1 = get_player_pos()
    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")
    d1 = math.sqrt(p1[0] ** 2 + p1[1] ** 2 + p1[2] ** 2)
    print(f"Distance to center: {round(d1, 4)}")
    print()
    print("Get a second set of coordinates")
    p2 = get_player_pos()
    d2 = math.sqrt(
        (p2[0] - p1[0]) ** 2
        + (p2[1] - p1[1]) ** 2
        + (p2[2] - p1[2]) ** 2
    )
    print(f"Distance between the 2 sets of coordinates: {round(d2, 4)}")


if __name__ == "__main__":
    main()
