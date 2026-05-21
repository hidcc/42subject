from .creature import Creature


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__(name="Aquabub", type_="Water")

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"
