from ex0.creature import Creature
from .capabilities import TransformCapability


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, name="Shiftling", type_="Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self._transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self.name} returns to normal."
