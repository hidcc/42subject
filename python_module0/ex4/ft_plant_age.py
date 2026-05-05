def ft_plant_age() -> None:
    check_harvest = int(input("Enter plant age in days: "))
    if check_harvest > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
