from dataclasses import dataclass
from enum import Enum, auto


class Mode(Enum):
    NORMAL = auto()
    INSERT = auto()
    SELECT = auto()


@dataclass(frozen=True, order=True)
class Position:
    row: int
    col: int


@dataclass
class Selection:
    anchor: Position
    head: Position

    @classmethod
    def cursor(cls, row: int, col: int) -> "Selection":
        pos = Position(row, col)
        return cls(anchor=pos, head=pos)

    @property
    def start(self) -> Position:
        return min(self.anchor, self.head)

    @property
    def end(self) -> Position:
        return max(self.anchor, self.head)

    @property
    def is_collapsed(self) -> bool:
        return self.anchor == self.head

    def contains(self, pos: Position) -> bool:
        return self.start <= pos <= self.end
    
