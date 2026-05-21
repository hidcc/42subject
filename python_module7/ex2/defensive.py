from .strategy import BattleStrategy


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature):
        return isinstance(creature, HealCapability)

    def act(self, creature):
        if not self.is_valid(creature):
            raise InvalidStrategyError()
        print(creature.attack())
        print(creature.heal())
