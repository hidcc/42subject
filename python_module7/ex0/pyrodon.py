from .creature import Creature


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Pyrodon", type_="Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"
