def ft_water_reminder() -> None:
    check_water_reminder = int(input("Days since last watering: "))
    if check_water_reminder > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
