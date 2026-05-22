from .strategy import BattleStrategy, InvalidStrategyError
from ex1.capabilities import HealCapability


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this defensive strategy"
            )
        print(creature.attack())
        print(creature.heal())
