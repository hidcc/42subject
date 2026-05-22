from .strategy import BattleStrategy, InvalidStrategyError
from ex1.capabilities import TransformCapability


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this aggressive strategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
