from editor.buffer import TextBuffer
from editor.models import Position

def test_buffer_init_empty():
    buf = TextBuffer()
    assert buf.lines == [""]
    assert buf.get_text() == ""
    assert buf.selection.head == Position(0, 0)


def test_buffer_init_multiline():
    buf = TextBuffer("hello\nworld")
    assert buf.lines == ["hello", "world"]
    assert buf.get_text() == "hello\nworld"


def test_buffer_move_and_clamp():
    buf = TextBuffer("abs\nde")

    buf.move(-1, -1)
    assert buf.selection.head == Position(0, 0)

    buf.move(0, 10)
    assert buf.selection.head == Position(0, 3)

    buf.move(1, 0)
    assert buf.selection.head == Position(1, 2)


def test_buffer_move_extend_selection():
    buf = TextBuffer("absdef")

    buf.move(0, 1)
    assert buf.selection.is_collapsed is True

    buf.move(0, 3, extend=True)
    assert buf.selection.anchor == Position(0, 1)
    assert buf.selection.head == Position(0, 4)
    assert buf.selection.is_collapsed is False

    buf.move(0, 1, extend=False)
    assert buf.selection.anchor == Position(0, 5)
    assert buf.selection.head == Position(0, 5)
    assert buf.selection.is_collapsed is True
