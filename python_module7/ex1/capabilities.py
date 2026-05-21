from abc import ABC, abstractmethod
from typing import Optional, Any


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: Optional[Any] = None) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self._transformed: bool = False

    @property
    def is_transformed(self) -> bool:
        return self._transformed

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
