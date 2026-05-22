from ex0.creature import Creature
from .capabilities import HealCapability


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__(name="Bloomelle", type_="Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: object | None = None) -> str:
        return f"{self.name} heals itself and others for a large amount"
