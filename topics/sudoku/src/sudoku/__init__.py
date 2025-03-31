import collections
import io
import itertools
import pathlib

EMPTY_CELL = "."


class SudokuBoard:
    def __init__(self):
        self.board = collections.defaultdict(lambda: EMPTY_CELL)

    def __str__(self):
        buf = io.StringIO()
        buf.write("┌───────┬───────┬───────┐\n")
        for row in range(9):
            buf.write("│")
            for col in range(9):
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
        yield from ((row, col2) for col2 in range(9) if col != col2)
        yield from ((row2, col) for row2 in range(9) if row != row2)

        start_row = row // 3 * 3
        start_col = col // 3 * 3
        for row2 in range(start_row, start_row + 3):
            for col2 in range(start_col, start_col + 3):
                if row != row2 and col != col2:
                    yield row2, col2

    def empty_cells(self):
        return (
            (row, col)
            for row, col in itertools.product(range(9), range(9))
            if self.board[row, col] == EMPTY_CELL
        )

    @classmethod
    def from_grid(cls, grid):
        me = cls()
        for row_number, column in enumerate(grid):
            for col_number, cell in enumerate(column):
                me.board[row_number, col_number] = cell
        return me


def load(path: str | pathlib.Path):
    path = pathlib.Path(path)
    assert path.exists()

    if path.suffix == ".ss":
        return load_ss(path)


def load_ss(path: str | pathlib.Path):
    path = pathlib.Path(path)
    assert path.exists()

    lines = []
    with open(path) as stream:
        for line in stream:
            line = line.strip().replace("|", "")
            if not line:
                continue
            if "-" in line:
                continue
            if line.startswith("#"):
                continue
            lines.append(line.split())

    return SudokuBoard.from_grid(lines)
