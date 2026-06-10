def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    avg = sum(map(lambda m: m['power'], mages)) / len(mages)
    return {
        'max_power': max(mages, key=lambda m: m['power'])['power'],
        'min_power': min(mages, key=lambda m: m['power'])['power'],
        'avg_power': round(avg, 2),
    }


def main() -> None:
    artifacts = [{'name': 'Storm Crown', 'power': 116, 'type': 'focus'},
                 {'name': 'Fire Staff', 'power': 111, 'type': 'weapon'},
                 {'name': 'Fire Staff', 'power': 81, 'type': 'accessory'},
                 {'name': 'Crystal Orb', 'power': 105, 'type': 'focus'}]
    mages = [{'name': 'Riley', 'power': 78, 'element': 'wind'},
             {'name': 'Phoenix', 'power': 95, 'element': 'shadow'},
             {'name': 'Casey', 'power': 68, 'element': 'shadow'},
             {'name': 'Storm', 'power': 93, 'element': 'water'},
             {'name': 'Riley', 'power': 84, 'element': 'shadow'}]
    spells = ['lightning', 'heal', 'blizzard', 'earthquake']

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    first, second = sorted_artifacts[0], sorted_artifacts[1]
    print(f"{first['name']} ({first['power']} power) "
          f"comes before {second['name']} ({second['power']} power)")
    print()

    print("Testing power filter...")
    strong_mages = power_filter(mages, 80)
    for mage in strong_mages:
        print(f"{mage['name']}: {mage['power']} power")
    print()

    print("Testing spell transformer...")
    transformed = spell_transformer(spells)
    print(" ".join(transformed))
    print()

    print("Testing mage stats...")
    stats = mage_stats(mages)
    for key, value in stats.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
