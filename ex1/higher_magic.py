from collections.abc import Callable
from typing import Tuple, List


def is_strong_enough(target: str, power: int) -> bool:
    return power >= 50


def fireball(target: str, power: int) -> str:
    return f"Fireball cast on {target} with {power} power!"


def heal(target: str, power: int) -> str:
    return f"Heal cast on {target} for {power} health points!"


def shield(target: str, power: int) -> str:
    return f"Shield raised around {target} with {power} durability!"


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str],
) -> Callable[[str, int], Tuple[str, str]]:
    def combined_spell(target: str, power: int) -> Tuple[str, str]:
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return (res1, res2)

    return combined_spell


def power_amplifier(
    spell: Callable[[str, int], str],
    factor: int,
) -> Callable[[str, int], str]:
    def amplified_spell(target: str, power: int) -> str:
        boosted_power = power * factor
        return spell(target, boosted_power)

    return amplified_spell


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str],
) -> Callable[[str, int], str]:
    def guarded_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"

    return guarded_spell


def spell_sequence(
    spells: List[Callable[[str, int], str]],
) -> Callable[[str, int], List[str]]:
    def execute_all(target: str, power: int) -> List[str]:
        return [spell(target, power) for spell in spells]

    return execute_all


def main():
    target_dummy = "Practice Golem"
    base_power = 25

    print("--- 1. Testing spell_combiner ---")
    dual_cast = spell_combiner(fireball, shield)
    results = dual_cast(target_dummy, base_power)
    print(f"Dual Cast Results: {results}")

    print("\n--- 2. Testing power_amplifier ---")
    great_staff_fireball = power_amplifier(fireball, 3)
    amplified_result = great_staff_fireball(target_dummy, base_power)
    print(f"Amplified Spell: {amplified_result}")

    print("\n--- 3. Testing conditional_caster ---")
    def strong_condition(t, p): return p >= 50
    elite_heal = conditional_caster(strong_condition, heal)

    print(f"Casting with 25 power: {elite_heal(target_dummy, base_power)}")
    print(f"Casting with 60 power: {elite_heal(target_dummy, 60)}")

    print("\n--- 4. Testing spell_sequence ---")
    barrage_list = [fireball, heal, shield]
    barrage_cast = spell_sequence(barrage_list)

    all_results = barrage_cast(target_dummy, base_power)
    print("Full Barrage Results:")
    for i, res in enumerate(all_results, 1):
        print(f"  {i}. {res}")


if __name__ == "__main__":
    main()
