"""Tests for the Connection domain model."""
import pytest

from flyin.domain.connection import Connection


def test_key_is_order_independent() -> None:
    """a-b and b-a share the same key (used for duplicate detection)."""
    assert Connection("a", "b").key == Connection("b", "a").key


def test_other_returns_opposite_endpoint() -> None:
    """other() returns the endpoint opposite to the one given, both ways."""
    c = Connection("roof1", "roof2")
    assert c.other("roof1") == "roof2"
    assert c.other("roof2") == "roof1"


def test_other_unknown_endpoint_raises() -> None:
    """Asking for the opposite of a non-endpoint raises ValueError."""
    with pytest.raises(ValueError):
        Connection("a", "b").other("c")


def test_self_loop_raises() -> None:
    """A zone cannot be connected to itself."""
    with pytest.raises(ValueError):
        Connection("a", "a")


def test_invalid_capacity_raises() -> None:
    """max_link_capacity below 1 violates a domain invariant."""
    with pytest.raises(ValueError):
        Connection("a", "b", max_link_capacity=0)


def test_default_capacity() -> None:
    """A bare connection has a capacity of 1."""
    assert Connection("a", "b").max_link_capacity == 1
