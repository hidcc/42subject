import alchemy
from alchemy import elements


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew '{create_air()}' and '{strength_potion()}'
            mixed with '{create_fire()}'")
