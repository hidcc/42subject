class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float,
    ) -> None:
        self.name = name
        self._height = float(height)
        self._age = age
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def grow(self) -> None:
        self._height = round(self._height + self.growth_rate, 2)

    def age(self) -> None:
        self._age += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30, 0.8)
    print("=== Garden Plant Growth ===")
    rose.show()

    start_height = rose.get_height()

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        rose.show()
    total = round(rose.get_height() - start_height, 2)
    print(f"Growth this week: {total}cm")
