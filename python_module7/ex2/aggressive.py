from .strategy import BattleStrategy
from ex1.capabilities import TransformCapability


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature):
        return isinstance(creature, TransformCapability)

    def act(self, creature):
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this aggressive strategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
