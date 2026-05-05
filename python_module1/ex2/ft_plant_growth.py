class Plant:
    name: str
    _height: float
    _age: int
    growth_rate: float

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def grow(self) -> None:
        self._height = round(self._height + self.growth_rate, 2)

    def age(self) -> None:
        self._age += 1


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose._height = 25.0
    rose._age = 30
    rose.growth_rate = 0.8

    print("=== Garden Plant Growth ===")
    rose.show()

    start_height = rose._height

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        rose.show()
    total = round(rose._height - start_height, 2)
    print(f"Growth this week: {total}cm")
