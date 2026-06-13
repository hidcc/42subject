"""Network domain model: the graph of zones and their connections."""
from abc import ABC, abstractmethod
from collections.abc import Iterable

from .zone import Zone
from .connection import Connection


class NetWorkView(ABC):
    """Read-only view of the network."""

    @abstractmethod
    def zones(self) -> Iterable[Zone]:
        """Return all zones in the network."""

    @abstractmethod
    def zone(self, name: str) -> Zone:
        """Return the zone with the given name."""

    @abstractmethod
    def neighbors(self, name: str) -> Iterable[Zone]:
        """Return the zones directly connected to the given zone."""

    @abstractmethod
    def connection(self, a: str, b: str) -> Connection:
        """Return the connection linking two zones."""

    @property
    @abstractmethod
    def start(self) -> Zone:
        """Return the unique start zone."""

    @property
    @abstractmethod
    def end(self) -> Zone:
        """Return the unique end zone."""


class NetWork(NetWorkView):
    """Mutable network. Only the parser/builder adds to it."""

    def __init__(self) -> None:
        """Create an empty network."""
        self._zones: dict[str, Zone] = {}
        self._connections: dict[frozenset[str], Connection] = {}
        self._adjencty: dict[str, list[str]] = {}

    def add_zone(self, zone: Zone) -> None:
        "Register a zone. Raise if the name is already used."
        if zone.name in self._zones:
            raise ValueError(f"duplicate zone name {zone.name}")
        self._zones[zone.name] = zone
        self._adjencty[zone.name] = []

    def add_connetion(self, connection: Connection) -> None:
        """Register a connection between two already defined zones."""
        for endpoint in connection.a, connection.b:
            if endpoint not in self._zones:
                raise ValueError(f"connection to unknown zones: {endpoint}")
        if connection.key in self._connections:
            raise ValueError(f"duplicate connection: {connection.a}-{connection.b}")
        self._connections[connection.key] = connection
        self._adjencty[connection.a].append(connection.b)
        self._adjencty[connection.b].append(connection.a)

    def zones(self) -> Iterable[Zone]:
        """Return all zones in the network."""
        return self._zones.values()

    def zone(self, name: str) -> Zone:
        """Return the zone with the given name."""
        if name not in self._zones:
            raise KeyError(f"unknown zone: {name}")
        return self._zones[name]

    def neighbors(self, name: str) -> Iterable[Zone]:
        """Return the zones directly connected to the given name."""
        return [self._zones[n] for n in self._adjencty[name]]

    def connection(self, a: str, b: str) -> Connection:
        """Return the connection linking two zones."""
        key = frozenset((a, b))
        if key not in self._connections:
            raise KeyError(f"no connection between {a} and {b}")
        return self._connections[key]

    @property
    def start(self) -> Zone:
        """Return the unique start zone."""
        return next(z for z in self._zones.values() if z.is_start)

    @property
    def end(self) -> Zone:
        """Return the unique end zone."""
        return next(z for z in self._zones.values() if z.is_end)
