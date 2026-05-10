class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float = 0.5
    ) -> None:
        self.name = name
        self._height = height
        self._age = age
        self.growth_rate = growth_rate
        print("Created: ", end="")
        self.show()

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def grow(self) -> None:
        self._height = round(self._height + self.growth_rate, 2)

    def age(self) -> None:
        self._age += 1


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    Plant("Rose", 25.0, 30)
    Plant("Oak", 200.0, 365)
    Plant("Cactus", 5.0, 90)
    Plant("Sunflower", 80.0, 45)
    Plant("Fern", 15.0, 120)
