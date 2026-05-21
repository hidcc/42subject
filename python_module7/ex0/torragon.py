from .creature import Creature


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Torragon", type_="Water")

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"
