import random

ACHIEVEMENTS = (
    "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
    "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
    "First Steps", "Collector Supreme", "Untouchable",
    "Hidden Path Finder", "Sharp Mind", "Boss Slayer",
)


def gen_player_achievements() -> set[str]:
    n = random.randint(7, 9)
    picked = random.sample(ACHIEVEMENTS, n)
    return set(picked)


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()
    PlayerA = gen_player_achievements()
    print(f"Player Alice: {PlayerA}")
    PlayerB = gen_player_achievements()
    print(f"Player Bob: {PlayerB}")
    PlayerC = gen_player_achievements()
    print(f"Player Charlie: {PlayerC}")
    PlayerD = gen_player_achievements()
    print(f"Player Dylan: {PlayerD}")
    print()
    distinct = set.union(PlayerA, PlayerB, PlayerC, PlayerD)
    print(f"All distinct achievements: {distinct}")
    print()
    common = set.intersection(PlayerA, PlayerB, PlayerC, PlayerD)
    print(f"Common achievements: {common}")
    print()
    diffa = set.difference(PlayerA, PlayerB, PlayerC, PlayerD)
    diffb = set.difference(PlayerB, PlayerA, PlayerC, PlayerD)
    diffc = set.difference(PlayerC, PlayerB, PlayerA, PlayerD)
    diffd = set.difference(PlayerD, PlayerB, PlayerC, PlayerA)
    print(f"Only Alice has: {diffa}")
    print(f"Only Bob has: {diffb}")
    print(f"Only Charlie has: {diffc}")
    print(f"Only Dylan has: {diffd}")
    print()
    pool = set(ACHIEVEMENTS)
    print(f"Alice is missing: {set.difference(pool, diffa)}")
    print(f"Bob is missing: {set.difference(pool, diffb)}")
    print(f"Charlie is missing: {set.difference(pool, diffc)}")
    print(f"Dylan is missing: {set.difference(pool, diffd)}")


if __name__ == "__main__":
    main()
