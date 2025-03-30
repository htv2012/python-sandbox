import collections
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
