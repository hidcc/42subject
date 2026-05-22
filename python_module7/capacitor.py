from ex1 import HealingCreatureFactory, TransformCreatureFactory


def heal_test(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())
    print()


def transform_test(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    print(" base:")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


heal_test(HealingCreatureFactory())
transform_test(TransformCreatureFactory())
