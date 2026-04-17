
"""Closure = inner function remembers outer variable (nonlocal)"""


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

    def power_addition(amount: int) -> int:
        """Add `amount` to the running total and return the new total."""
        nonlocal total_power
        total_power += amount
        return total_power

    return power_addition


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchanted_info(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchanted_info


def memory_vault() -> dict[str, Callable[..., Any]]:
    memory: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        """Store a value under `key` in the vault."""
        memory[key] = value

    def recall(key: str) -> Any:
        """Return stored value or a sentinel message when missing."""
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main():
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")

    print("\nTesting enchantment factory...")
    flame_factory = enchantment_factory("Flaming")
    frost_factory = enchantment_factory("Frozen")

    print(flame_factory("Sword"))
    print(frost_factory("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()

    print("Store 'secret' = 42")
    vault["store"]("secret", 42)

    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
