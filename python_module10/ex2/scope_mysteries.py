from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def add_spell(add_power: int) -> int:
        nonlocal total_power
        total_power += add_power
        return total_power
    return add_spell


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    memories: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memories[key] = value

    def recall(key: str) -> Any:
        return memories.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    initial_powers = [66, 53, 40]
    power_additions = [18, 16, 20, 11, 17]
    enchantment_types = ['Radiant', 'Windy', 'Dark']
    items_to_enchant = ['Sword', 'Ring', 'Amulet', 'Armor']
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print("==========================")
    print("Testing spell accumulator...")
    for ini in initial_powers:
        accumulator = spell_accumulator(ini)
        print(f"initial power is {ini}")
        for power in power_additions:
            print(f"add {power}: {accumulator(power)}")
        print("==========================")
    print("Testing enchantment factory...")
    for type_ in enchantment_types:
        enchant = enchantment_factory(type_)
        for item in items_to_enchant:
            print(f"{enchant(item)}")
        print("==========================")

    print("Testing memory vault...")
    vault = memory_vault()
    vault["store"]("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
