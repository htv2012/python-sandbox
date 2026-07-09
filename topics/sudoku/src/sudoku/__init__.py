import collections
import io
import itertools
import pathlib
import re

EMPTY_CELL = "."
ROW_INDICES = list(range(9))
COL_INDICES = list(range(9))


class SudokuBoard:
    def __init__(self):
        self.board = collections.defaultdict(lambda: EMPTY_CELL)

    def __str__(self):
        buf = io.StringIO()
        buf.write("┌───────┬───────┬───────┐\n")
        for row in ROW_INDICES:
            buf.write("│")
            for col in COL_INDICES:
                buf.write(f" {self.board[row, col]}")
                if col == 2 or col == 5 or col == 8:
                    buf.write(" │")
            buf.write("\n")
            if row == 2 or row == 5:
                buf.write("│───────┼───────┼───────│\n")
        buf.write("└───────┴───────┴───────┘")
        return buf.getvalue()

    def solve(self) -> bool:
        for row, col in self.empty_cells():
            for candidate in "123456789":
                if self.conflicted(row, col, candidate):
                    continue
                self.board[row, col] = candidate
                if self.solve():
                    return True
            self.board[row, col] = EMPTY_CELL
            return False
        return True

    def conflicted(self, row, col, candidate):
        return any(
            self.board[row2, col2] == candidate
            for row2, col2 in self.neighbors(row, col)
        )

    def neighbors(self, row, col):
        yield from ((row, col2) for col2 in COL_INDICES if col != col2)
        yield from ((row2, col) for row2 in ROW_INDICES if row != row2)

        start_row = row // 3 * 3
        start_col = col // 3 * 3
        for row2 in range(start_row, start_row + 3):
            for col2 in range(start_col, start_col + 3):
                if row != row2 and col != col2:
                    yield row2, col2

    def empty_cells(self):
        return (
            (row, col)
            for row, col in itertools.product(ROW_INDICES, COL_INDICES)
            if self.board[row, col] == EMPTY_CELL
        )

    @classmethod
    def from_grid(cls, grid):
        me = cls()
        for row_number, column in enumerate(grid):
            for col_number, cell in enumerate(column):
                me.board[row_number, col_number] = cell
        return me

    @classmethod
    def from_sequence(cls, sequence):
        me = cls()
        seq = iter(sequence)
        for row_number in ROW_INDICES:
            for col_number in COL_INDICES:
                me.board[row_number, col_number] = next(seq)
        return me


def load(path: str | pathlib.Path):
    path = pathlib.Path(path)
    assert path.exists()

    with open(path) as stream:
        sequence = re.findall(r"[123456789.]", stream.read())

    if (actual := len(sequence)) != 81:
        raise ValueError(f"Expect 81 values in {path}, got {actual}")
    puzzle = SudokuBoard.from_sequence(sequence)
    return puzzle


def dump(puzzle: SudokuBoard, filename: str | pathlib.Path):
    """Dump (serialize) a Sudoku puzzle, only support *.ss format."""
    path = pathlib.Path(filename)
    if path.suffix != ".ss":
        raise ValueError(f"Expect filename which ends with .ss, not {filename}")

    text = str(puzzle)
    t = {
        "┌": "*",
        "┐": "*",
        "└": "*",
        "┘": "*",
        "┬": "-",
        "┴": "-",
        "┼": "+",
        "│": "|",
        "─": "-",
    }
    for old, new in t.items():
        text = text.replace(old, new)
    path.write_text(text + "\n")
