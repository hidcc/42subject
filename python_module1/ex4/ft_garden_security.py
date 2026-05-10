class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float = 0.5,
    ) -> None:
        self.name = name
        self.growth_rate = growth_rate
        if height < 0:
            print(f"{name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = float(height)
        if age < 0:
            print(f"{name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return
        self._height = float(height)

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            return
        self._age = age

    def grow(self) -> None:
        self._height = round(self._height + self.growth_rate, 2)

    def age(self) -> None:
        self._age += 1


if __name__ == "__main__":
    print("=== Garde Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print()

    rose.set_height(25)
    print(f"Height updated: {rose.get_height():.0f}cm")
    rose.set_age(30)
    print(f"Age updated: {rose.get_age()} days")
    print()

    rose.set_height(-5)
    print("Height update rejected")
    rose.set_age(-3)
    print("Age update rejected")
    print()

    print("Current state: ", end="")
    rose.show()
