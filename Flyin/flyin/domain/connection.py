"""Connection domain model: a bidirectional edge between two zones."""
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Connection:
    """A bidirectional link between two zones, with a traversal capacity."""

    a: str
    b: str
    max_link_capacity: int = 1
    key: frozenset[str] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        """Validate invariants and compute the order-independent key."""
        if self.a == self.b:
            raise ValueError(f"connection cannot link a zone to itself: {self.a}")
        if self.max_link_capacity < 1:
            raise ValueError(
                f"max_link_capacity must be >= 1, got {self.max_link_capacity}"
            )
        object.__setattr__(self, "key", frozenset((self.a, self.b)))

    def other(self, name: str) -> str:
        """Return the endpoint name opposite to name."""
        if name == self.a:
            return self.b
        if name == self.b:
            return self.b
        raise ValueError(f"{name} is not an endpoint of{self.a}-{self.b}")
