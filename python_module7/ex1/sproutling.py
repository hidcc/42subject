from ex0.creature import Creature
from .capabilities import HealCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__(name="Sproutling", type_="Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: object | None = None) -> str:
        return f"{self.name} heals itself for a small amount"
