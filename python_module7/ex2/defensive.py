from .strategy import BattleStrategy, InvalidStrategyError
from ex0.creature import Creature
from ex1.capabilities import HealCapability


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, HealCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this defensive strategy"
            )
        print(creature.attack())
        print(creature.heal())
