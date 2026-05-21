from .strategy import BattleStrategy


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature):
        return True

    def act(self, creature):
        if not self.is_valid(creature):
            raise InvalidStrategyError()
        print(creature.attack())
