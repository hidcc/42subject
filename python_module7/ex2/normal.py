from .strategy import BattleStrategy, InvalidStrategyError
from ex0.creature import Creature


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError()
        print(creature.attack())
