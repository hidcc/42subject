def ft_count_harvest_iterative() -> None:
    count = int(input("Days until harvest: "))
    for i in range(count):
        print(f"Day {i + 1}")
    print("Harvest time!")
