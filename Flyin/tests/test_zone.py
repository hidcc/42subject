"""Tests for the Zone domain model."""
import sys

import pytest

from flyin.domain.zone import Zone, ZoneType


def test_zonetype_from_string() -> None:
    """ZoneType is constructible from its string value."""
    assert ZoneType("normal") is ZoneType.NORMAL
    assert ZoneType("restricted") is ZoneType.RESTRICTED


def test_zonetype_invalid_string_raises() -> None:
    """An unknown zone-type string raises ValueError (parser maps to ParseError)."""
    with pytest.raises(ValueError):
        ZoneType("teleport")


def test_traversal_turns() -> None:
    """Only restricted zones cost 2 turns; the rest cost 1."""
    assert ZoneType.NORMAL.traversal_turns() == 1
    assert ZoneType.PRIORITY.traversal_turns() == 1
    assert ZoneType.BLOCKED.traversal_turns() == 1
    assert ZoneType.RESTRICTED.traversal_turns() == 2


def test_is_accessible() -> None:
    """Only blocked zones are inaccessible."""
    assert ZoneType.NORMAL.is_accessible() is True
    assert ZoneType.PRIORITY.is_accessible() is True
    assert ZoneType.RESTRICTED.is_accessible() is True
    assert ZoneType.BLOCKED.is_accessible() is False


def test_zone_defaults() -> None:
    """A bare zone uses the documented defaults."""
    z = Zone("hub", 1, 2)
    assert z.zone_type is ZoneType.NORMAL
    assert z.color is None
    assert z.max_drones == 1
    assert z.is_start is False
    assert z.is_end is False


def test_capacity_normal() -> None:
    """A normal zone's capacity equals its max_drones."""
    assert Zone("a", 0, 0, max_drones=3).capacity() == 3


def test_capacity_start_end_unlimited() -> None:
    """Start and end zones have unlimited capacity."""
    assert Zone("s", 0, 0, is_start=True).capacity() == sys.maxsize
    assert Zone("e", 0, 0, is_end=True).capacity() == sys.maxsize


def test_invalid_max_drones_raises() -> None:
    """max_drones below 1 violates a domain invariant."""
    with pytest.raises(ValueError):
        Zone("a", 0, 0, max_drones=0)
