import pytest
from dataclasses import FrozenInstanceError

from editor.models import Position, Selection

def test_position_ordering():
    p1 = Position(0, 5)
    p2 = Position(0, 10)
    p3 = Position(1, 0)

    assert p1 < p2
    assert p2 < p3
    assert p1 == Position(0, 5)


def test_position_is_immutable():
    pos = Position(1, 2)
    with pytest.raises(FrozenInstanceError):
        pos.row = 5


def test_selection_cursor():
    sel = Selection.cursor(2, 4)

    assert sel.anchor == Position(2, 4)
    assert sel.head == Position(2, 4)
    assert sel.start == Position(2, 4)
    assert sel.end == Position(2, 4)
    assert sel.is_collapsed is True
    assert sel.contains(Position(2, 4)) is True
    assert sel.contains(Position(2, 5)) is False


def test_selection_forward():
    sel = Selection(anchor=Position(0, 2), head=Position(0, 6))

    assert sel.start == Position(0, 2)
    assert sel.end == Position(0, 6)
    assert sel.is_collapsed is False
    assert sel.contains(Position(0, 2)) is True
    assert sel.contains(Position(0, 4)) is True
    assert sel.contains(Position(0, 6)) is True
    assert sel.contains(Position(0, 1)) is False
    assert sel.contains(Position(0, 7)) is False


def test_selection_backward():
    sel = Selection(anchor=Position(0, 6), head=Position(0, 2))

    assert sel.start == Position(0, 2)
    assert sel.end == Position(0, 6)
    assert sel.is_collapsed is False
    assert sel.contains(Position(0, 4)) is True


def test_selection_multiline():
    sel = Selection(anchor=Position(1, 5), head=Position(3, 2))

    assert sel.contains(Position(1, 4)) is False
    assert sel.contains(Position(1, 5)) is True
    assert sel.contains(Position(2, 0)) is True
    assert sel.contains(Position(3, 2)) is True
    assert sel.contains(Position(3, 3)) is False
