"""Zone domain model: a node in the drone network."""
import sys
from dataclasses import dataclass
from enum import Enum


class ZoneType(Enum):
    """type of a zone, with its movement semantics."""
    NORMAL = "normal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "priority"

    def is_accessible(self) -> bool:
        """Return whether a drone may enter this kind of zone."""
        return self is not ZoneType.BLOCKED

    def traversal_turns(self) -> int:
        """Return how many turns a move into this kind of zone takes."""
        return 2 if self is ZoneType.RESTRICTED else 1


@dataclass(frozen=True)
class Zone:
    """A node in the network: a named position with a type and capacity."""
    name: str
    x: int
    y: int
    zone_type: ZoneType = ZoneType.NORMAL
    color: str | None = None
    max_drones: int = 1
    is_start: bool = False
    is_end: bool = False

    def __post_init__(self) -> None:
        """Validates invariants that hold regardless of input source."""
        if self.max_drones < 1:
            raise ValueError(f"max_drones must be >= 1, got {self.max_drones}")

    def capacity(self) -> int:
        """Return max drones allowed at once (start/end are unlimited)."""
        if self.is_start or self.is_end:
            return sys.maxsize
        return self.max_drones
