import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    print()
    initial_list = ['Alice', 'bob', 'Charlie', 'dylan',
                    'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {initial_list}")
    capitalized = [player.capitalize() for player in initial_list]
    print(f"New list with all names capitalized: {capitalized}")
    capitalized_already = [
        player for player in initial_list if player[0].upper() == player[0]]
    print(f"New list of capitalized names only: {capitalized_already}")
    print()
    score_dict = {name: random.randint(40, 1000) for name in capitalized}
    print(f"Score dict: {score_dict}")
    score_average = sum(score_dict[name]
                        for name in score_dict) / len(score_dict)
    print(f"Score average is {round(score_average, 2)}")
    high_scores = {name: score_dict[name]
                   for name in score_dict if score_dict[name] > score_average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
