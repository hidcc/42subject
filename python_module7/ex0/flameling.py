from .creature import Creature


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__(name="Flameling", type_="Fire")

    def attack(self) -> str:
        return f"{self.name} uses Ember!"
