from .strategy import BattleStrategy, InvalidStrategyError
from ex0.creature import Creature
from ex1.capabilities import TransformCapability


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this aggressive strategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
