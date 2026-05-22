from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (BattleStrategy, InvalidStrategyError,
                 NormalStrategy, AggressiveStrategy, DefensiveStrategy)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]
            creature1 = factory1.create_base()
            creature2 = factory2.create_base()
            print("* Battle *")
            print(creature1.describe())
            print(" vs.")
            print(creature2.describe())
            print(" now fight!")
            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                print()
                return
            print()


print("Tournament 0 (basic)")
print(" [ (Flameling+Normal), (Healing+Defensive) ]")
battle([(FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())])

print("Tournament 1 (error)")
print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
battle([(FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())])

print("Tournament 2 (multiple)")
print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
battle([(AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())])
