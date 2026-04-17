
"""Decorator = wrapper that adds behavior (@functools.wraps is mandatory)"""

import time
import functools
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"Spell completed in {duration:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            # check if called from the class method or not
            power = None
            if len(args) > 0 and isinstance(args[0], int):
                power = args[0]
            elif len(args) > 1 and isinstance(args[1], int):
                power = args[1]

            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exc: Exception | None = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    last_exc = exc
                    if attempt < max_attempts:
                        msg = (
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
                        print(msg)
                    else:
                        msg = (
                            "Spell casting failed after "
                            f"{max_attempts} attempts"
                        )
                        print(msg)
            # Re-raise the last exception after attempts
            if last_exc is not None:
                return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main():
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print("\nTesting retrying spell...")

    @retry_spell(max_attempts=3)
    def waaaaaaagh_spell():
        raise Exception("Waaaaaaagh spelled !")

    print(waaaaaaagh_spell())

    print("\nTesting MageGuild...")
    guild = MageGuild()

    print(guild.validate_mage_name("Alice"))
    print(guild.validate_mage_name("Al"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
