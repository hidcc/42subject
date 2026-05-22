from .strategy import BattleStrategy, InvalidStrategyError


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return True

    def act(self, creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError()
        print(creature.attack())
