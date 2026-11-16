from editor.models import Position, Selection


class TextBuffer:
    def __init__(self, text: str = "") -> None:
        self.lines: list[str] = text.split("\n") if text else [""]
        self.selection: Selection = Selection.cursor(0, 0)

    def get_text(self) -> str:
        return "\n".join(self.lines)

    def _clamp(self, pos: Position) -> Position:
        row = max(0, min(pos.row, len(self.lines) - 1))
        col = max(0, min(pos.col, len(self.lines[row])))
        return Position(row, col)

    def move(self, d_row: int, d_col: int, extend: bool = False) -> None:
        target = Position(
            row=self.selection.head.row + d_row,
            col=self.selection.head.col + d_col
        )
        new_head = self._clamp(target)

        if extend:
            self.selection = Selection(
                anchor=self.selection.anchor,
                head=new_head
            )
        else:
            self.selection = Selection.cursor(new_head.row, new_head.col)

        
