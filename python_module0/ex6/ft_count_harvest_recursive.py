def count_day(current: int, total: int) -> None:
    if current > total:
        print("Harvest time!")
        return
    print(f"Day {current}")
    count_day(current + 1, total)


def ft_count_harvest_recursive() -> None:
    count = int(input("Days until harvest: "))
    count_day(1, count)
