from ex0.factory import CreatureFactory
from .bloomelle import Bloomelle
from .morphagon import Morphagon
from .shiftling import Shiftling
from .sproutling import Sproutling


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
