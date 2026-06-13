"""Tests for the map text parser (TDD: drives the parser implementation)."""
from pathlib import Path

from flyin.adapters.parsing.map_parser import TextMapParser

MAPS = Path(__file__).resolve().parent.parent / "maps"


def test_parse_linear_path() -> None:
    """The simple linear map parses into the expected network."""
    text = (MAPS / "easy" / "01_linear_path.txt").read_text()
    result = TextMapParser().parse(text)

    assert result.nb_drones == 2
    assert result.network.start.name == "start"
    assert result.network.end.name == "goal"
    assert {z.name for z in result.network.zones()} == {
        "start",
        "waypoint1",
        "waypoint2",
        "goal",
    }
    assert result.network.zone("waypoint1").color == "blue"
    assert [z.name for z in result.network.neighbors("start")] == ["waypoint1"]
