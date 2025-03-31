import collections
import itertools
import io
import pathlib

EMPTY_CELL = "."


class Sudoku:
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

    def empties(self):
        return (
            (row, col)
            for row, col in itertools.product(range(9), range(9))
            if self.board[row, col] == EMPTY_CELL
        )

    def conflicted(self, row, col):
        candidate = self.board[row, col]

        # Check row
        if any(self.board[r, col] == candidate for r in range(9) if r != row):
            return True
        # Check col
        if any(self.board[row, c] == candidate for c in range(9) if c != col):
            return True


    def solve(self) -> bool:
        for row, col in self.empties():
            for candidate in '123456789':
                self.board[row, col] = candidate
                if not self.conflicted(row, col) and self.solve():
                    return True
            self.board[row, col] = EMPTY_CELL
            return False
        return True


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

    return Sudoku.from_grid(lines)
