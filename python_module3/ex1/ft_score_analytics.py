import sys


def score_process(scores: list[int]) -> None:
    print(f"Scores processed: {scores}")


def total_players(scores: list[int]) -> None:
    print(f"Total players: {len(scores)}")


def total_score(scores: list[int]) -> None:
    print(f"Total score: {sum(scores)}")


def average_score(scores: list[int]) -> None:
    print(f"Average score: {sum(scores) / len(scores)}")


def high_score(scores: list[int]) -> None:
    print(f"High score: {max(scores)}")


def low_score(scores: list[int]) -> None:
    print(f"Low score: {min(scores)}")


def score_range(scores: list[int]) -> None:
    print(f"Score range: {max(scores) - min(scores)}")


def parse_scores(args: list[str]) -> list[int]:
    scores: list[int] = []
    for arg in args[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return scores


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    args = sys.argv
    scores = parse_scores(args)
    if not scores:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        score_process(scores)
        total_players(scores)
        total_score(scores)
        average_score(scores)
        high_score(scores)
        low_score(scores)
        score_range(scores)
