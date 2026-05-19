from elements import create_fire
from alchemy.elements import create_air
from alchemy.potions import strength_potion


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: "
        f"brew '{create_air()}' and '{strength_potion()}' "
        f"mixed with '{create_fire()}'"
    )
