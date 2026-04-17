import functools
from functools import partial, lru_cache, singledispatch
from collections.abc import Callable
from typing import Any
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    ops: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: max(a, b),
        "min": lambda a, b: min(a, b),
    }

    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")

    return functools.reduce(ops[operation], spells)


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"Enchanting {target} with {element} power level {power}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_enchanter = partial(base_enchantment, 50, "Fire")
    ice_enchanter = partial(base_enchantment, 50, "Ice")
    lightning_enchanter = partial(base_enchantment, 50, "Lightning")

    return {
        "fire": fire_enchanter,
        "ice": ice_enchanter,
        "lightning": lightning_enchanter
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def cast(spell_input: Any) -> str:
        return f"Unknown spell type: {type(spell_input).__name__}"

    @cast.register(int)
    def _(power: int) -> str:
        return f"Damage spell: {power} damage!"

    @cast.register(str)
    def _(name: str) -> str:
        return f"Enchantment: {name}"

    @cast.register(list)
    def _(spells: list) -> str:
        return (
                f"Multi-casting ({len(spells)} spells): "
                f"{', '.join(map(str, spells))}"
                )

    return cast


def main() -> None:
    print("Testing spell reducer...")
    powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")

    print("\nTesting partial enchanters...")
    enchanters = partial_enchanter(base_enchantment)

    fire = enchanters["fire"]
    ice = enchanters["ice"]
    lightning = enchanters["lightning"]

    print(fire("Iron Sword"))
    print(ice("Crystal Shield"))
    print(lightning("Silver Dagger"))

    print("\nTesting memoized fibonacci...")
    for i in [0, 1, 10, 15]:
        print(f"Fib({i}): {memoized_fibonacci(i)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher(12.5))


if __name__ == "__main__":
    main()
