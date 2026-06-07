from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not callable(spell1) or not callable(spell2):
        raise TypeError("spell_combiner expects two callable spells")

    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell):
        raise TypeError("power_amplifier expects a callable spell")

    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(condition) or not callable(spell):
        raise TypeError("conditional_caster expects callable arguments")

    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    if not all(callable(spell) for spell in spells):
        raise TypeError("spell_sequence expects a list of callable spells")

    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequence


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def has_enough_power(target: str, power: int) -> bool:
    return power >= 20


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    first, second = combined("Dragon", 50)
    print(f"Combined spell result: {first}, {second}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Goblin', 10)}")
    print(f"Amplified: {mega_fireball('Goblin', 10)}")

    print("\nTesting conditional caster...")
    careful_heal = conditional_caster(has_enough_power, heal)
    print(f"With 50 power: {careful_heal('Knight', 50)}")
    print(f"With 5 power: {careful_heal('Knight', 5)}")

    print("\nTesting spell sequence...")
    barrage = spell_sequence([fireball, heal, mega_fireball])
    for result in barrage("Lich", 25):
        print(f"- {result}")

    print("\nTesting invalid spell rejection...")
    try:
        spell_combiner("not a spell", heal)  # type: ignore[arg-type]
    except TypeError as error:
        print(f"Rejected: {error}")


if __name__ == "__main__":
    main()
