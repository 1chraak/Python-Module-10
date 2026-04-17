"""Lambda = short anonymous function (map, filter, sorted)"""

from typing import List, Dict, Union


def artifact_sorter(
    artifacts: List[Dict[str, Union[str, int]]]
) -> List[Dict[str, Union[str, int]]]:

    if not artifacts:
        raise ValueError("Artifacts list must not be empty!")

    sorted_by_power = sorted(
        artifacts,
        key=lambda artifact: artifact['power'],
        reverse=True
    )
    return sorted_by_power


def power_filter(
    mages: List[Dict[str, Union[str, int]]],
    min_power: int
) -> List[Dict[str, Union[str, int]]]:

    if not mages:
        raise ValueError("Mages list must not be empty!")

    # Fix: Added an 'isinstance' check to satisfy mypy's type safety
    filtered_by_power: List[Dict[str, Union[str, int]]] = list(filter(
        lambda mage: isinstance
        (mage['power'], int) and mage['power'] >= min_power,
        mages
    ))
    return filtered_by_power


def spell_transformer(
    spells: List[str]
) -> List[str]:

    if not spells:
        raise ValueError("Spells list must not be empty!")

    transformed_spells = list(map(
        lambda spell: "* " + spell + " *",
        spells
    ))
    return transformed_spells


def mage_stats(
    mages: List[Dict[str, Union[str, int]]]
) -> Dict[str, Union[int, float]]:

    if not mages:
        raise ValueError("Mages list must not be empty!")

    max_val = max(mages, key=lambda m: m['power'])['power']
    min_val = min(mages, key=lambda m: m['power'])['power']

    # Cast the sum/len to float for the average to satisfy Union[int, float]
    total_power = sum(map(lambda m: int(m['power']), mages))
    avg_power = round(total_power / len(mages), 2)

    return {
        "max_power": int(max_val),  # type: ignore
        "min_power": int(min_val),  # type: ignore
        "avg_power": avg_power
    }


def main():
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Wooden Wand', 'power': 40, 'type': 'weapon'}
    ]

    mages = [
        {'name': 'Aria', 'power': 90, 'element': 'air'},
        {'name': 'Zane', 'power': 75, 'element': 'fire'},
        {'name': 'Lumina', 'power': 88, 'element': 'light'}
    ]

    spells = ["ignite", "heal", "smite"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    if len(sorted_artifacts) >= 2:
        a1, a2 = sorted_artifacts[0], sorted_artifacts[1]
        print(
            f"{a1['name']} "
            f"({a1['power']} power) comes before "
            f"{a2['name']} ({a2['power']} power)"
            )

    print("\nTesting power filter (min 80)...")
    strong_mages = power_filter(mages, 80)
    for m in strong_mages:
        print(f"Mage {m['name']} passed the trial.")

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    # Using join with a space to match expected output example
    print(" ".join(transformed))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Stats: {stats}")


if __name__ == "__main__":
    main()
