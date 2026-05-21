from ex0.creature import Creature
from .capabilities import TransformCapability


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, name="Morphagon", type_="Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self._transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self.name} stabilizes its form."
