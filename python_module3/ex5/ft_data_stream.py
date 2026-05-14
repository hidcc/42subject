import random
import typing

PLAYERS = ("alice", "bob", "charlie", "dylan")
ACTIONS = ("run", "eat", "sleep", "grab",
           "move", "climb", "swim", "use", "release")


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)


def consume_event(
    lst: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(lst) > 0:
        idx = random.randrange(len(lst))
        event = lst[idx]
        del lst[idx]
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    g = gen_event()
    for i in range(1000):
        name, action = next(g)
        print(f"Event {i}: Player {name} did action {action}")
    events = [next(g) for _ in range(10)]
    print(f"Built list of 10 events: {events}")
    for ev in consume_event(events):
        print(f"Got event from list: {ev}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
