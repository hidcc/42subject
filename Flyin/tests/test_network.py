"""Tests for the Network domain model."""
import pytest

from flyin.domain.connection import Connection
from flyin.domain.network import Network
from flyin.domain.zone import Zone


def _sample() -> Network:
    """Build a minimal hub--goal network for reuse across tests."""
    n = Network()
    n.add_zone(Zone("hub", 0, 0, is_start=True))
    n.add_zone(Zone("goal", 9, 9, is_end=True))
    n.add_connection(Connection("hub", "goal"))
    return n


def test_start_and_end() -> None:
    """The unique start and end zones are reported correctly."""
    n = _sample()
    assert n.start.name == "hub"
    assert n.end.name == "goal"


def test_neighbors_are_bidirectional() -> None:
    """A connection makes both endpoints neighbors of each other."""
    n = _sample()
    assert [z.name for z in n.neighbors("hub")] == ["goal"]
    assert [z.name for z in n.neighbors("goal")] == ["hub"]


def test_connection_lookup_is_order_independent() -> None:
    """connection(a, b) finds the link regardless of argument order."""
    n = _sample()
    assert n.connection("goal", "hub").key == frozenset({"hub", "goal"})


def test_duplicate_zone_raises() -> None:
    """Re-adding a zone name is rejected."""
    n = Network()
    n.add_zone(Zone("a", 0, 0))
    with pytest.raises(ValueError):
        n.add_zone(Zone("a", 1, 1))


def test_connection_to_unknown_zone_raises() -> None:
    """A connection may only link already-defined zones."""
    n = Network()
    n.add_zone(Zone("a", 0, 0))
    with pytest.raises(ValueError):
        n.add_connection(Connection("a", "ghost"))


def test_duplicate_connection_raises_both_directions() -> None:
    """a-b and b-a are duplicates and the second is rejected."""
    n = _sample()
    with pytest.raises(ValueError):
        n.add_connection(Connection("goal", "hub"))


def test_unknown_zone_lookup_raises() -> None:
    """Looking up a missing zone raises KeyError."""
    with pytest.raises(KeyError):
        Network().zone("nope")
