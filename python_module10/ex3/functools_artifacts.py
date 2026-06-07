from functools import reduce, partial, singledispatch, lru_cache
from collections.abc import Callable
from typing import Any
import operator

OPS: dict[str, Callable[[int, int], int]] = {
    'add': operator.add,
    'multiply': operator.mul,
    'max': max,
    'min': min,
}


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation not in OPS:
        raise ValueError(f"Unknown operation: {operation}")
    return reduce(OPS[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    elements = ['fire', 'ice', 'lightning']
    return {
        element: partial(base_enchantment, 50, element)
        for element in elements
    }


def enchant(power: int, element: str, target: str) -> str:
    return f"{target} enchanted with {element} (power: {power})"


@lru_cache(maxsize=None)
def memorized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return memorized_fibonacci(n - 1) + memorized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast(arg: Any) -> str:
        return "Unknown spell type"

    @cast.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @cast.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @cast.register(list)
    def _(arg: list[Any]) -> str:
        return f"Multi-cast: {len(arg)} spells"

    return cast


def main() -> None:
    spell_powers = [38, 16, 25, 12, 48, 37]
    operations = ['add', 'multiply', 'max', 'min']
    print("Testing spell reducer...")
    for operation in operations:
        print(f"{operation}: {spell_reducer(spell_powers, operation)}")
    print()
    print("Testing partial enchanter...")
    enchanters = partial_enchanter(enchant)
    for element, enchanter in enchanters.items():
        print(f"{element}: {enchanter('sword')}")
    print()
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memorized_fibonacci(0)}")
    print(f"Fib(1): {memorized_fibonacci(1)}")
    print(f"Fib(10): {memorized_fibonacci(10)}")
    print(f"Fib(15): {memorized_fibonacci(15)}")
    print()
    print("Testing spell dispatcher...")
    a = spell_dispatcher()
    print(a(42))
    print(a("fireball"))
    print(a(spell_powers))
    print(a(3.14))


if __name__ == "__main__":
    main()
