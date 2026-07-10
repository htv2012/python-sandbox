import io
import itertools
import logging
import pathlib
import re
from collections.abc import MutableMapping

logger = logging.getLogger()

EMPTY_CELL = "."
ROW_INDICES = list(range(9))
COL_INDICES = list(range(9))
ALL_INDICES = list(itertools.product(ROW_INDICES, COL_INDICES))
REPLACEMENT_TABLE = [
    ("┌", "*"),
    ("┐", "*"),
    ("└", "*"),
    ("┘", "*"),
    ("┬", "-"),
    ("┴", "-"),
    ("┼", "+"),
    ("│", "|"),
    ("─", "-"),
]


class SudokuBoard(MutableMapping):
    def __init__(self):
        self.board = dict.fromkeys(ALL_INDICES, EMPTY_CELL)
        self.original = {}

    def solve(self) -> bool:
        for row, col in ALL_INDICES:
            if self[row, col] != EMPTY_CELL:
                continue
            for candidate in "123456789":
                if self.conflicted(row, col, candidate):
                    continue
                self[row, col] = candidate
                if self.solve():
                    return True
            self[row, col] = EMPTY_CELL
            return False
        return True

    def conflicted(self, row, col, candidate) -> bool:
        """Does this candidate causes a conflict?"""
        return any(
            self[row2, col2] == candidate for row2, col2 in self.neighbors(row, col)
        )

    def neighbors(self, row, col):
        """
        Return the neighbors of a given cell.

        This includes all the cells in the same row, all the cells
        in the same column, and all the cells in the same block.
        """
        yield from ((row, col2) for col2 in COL_INDICES if col != col2)
        yield from ((row2, col) for row2 in ROW_INDICES if row != row2)

        start_row = row // 3 * 3
        start_col = col // 3 * 3
        for row2 in range(start_row, start_row + 3):
            for col2 in range(start_col, start_col + 3):
                if row != row2 and col != col2:
                    yield row2, col2

    def save_original(self):
        self.original = {
            coord: value for coord, value in self.items() if self[coord] != EMPTY_CELL
        }

    @property
    def original_in_tact(self) -> bool:
        diff = [
            (row, col, expected)
            for (row, col), expected in self.original.items()
            if self[row, col] != expected
        ]
        if diff:
            for row, col, expected in diff:
                logger.debug(f"diff: {self[row, col]=} != {expected}")
        return not diff

    @property
    def is_valid(self):
        return all(
            self[row, col] == EMPTY_CELL
            or not self.conflicted(row, col, self[row, col])
            for row, col in ALL_INDICES
        )

    # ======================================================================
    # Support
    # ======================================================================

    def to_string(self, ascii: bool = False) -> str:
        buf = io.StringIO()
        buf.write("┌───────┬───────┬───────┐\n")
        for row in ROW_INDICES:
            buf.write("│")
            for col in COL_INDICES:
                buf.write(f" {self[row, col]}")
                if col == 2 or col == 5 or col == 8:
                    buf.write(" │")
            buf.write("\n")
            if row == 2 or row == 5:
                buf.write("│───────┼───────┼───────│\n")
        buf.write("└───────┴───────┴───────┘")

        text = buf.getvalue()
        if ascii:
            for old, new in REPLACEMENT_TABLE:
                text = text.replace(old, new)

        return text

    def __str__(self):
        return self.to_string()

    @classmethod
    def from_sequence(cls, sequence):
        """
        Create a new Sudoku puzzle from a sequence of values.

        The values can be '1' .. '9', and EMPTY_CELL.
        """
        me = cls()
        seq = iter(sequence)
        for row_number, col_number in ALL_INDICES:
            me.board[row_number, col_number] = next(seq)
        return me

    def __len__(self):
        return len(self.board)

    def __getitem__(self, key):
        return self.board[key]

    def __setitem__(self, key, value):
        self.board[key] = value

    def __delitem__(self, key):
        del self.board[key]

    def __iter__(self):
        return iter(self.board)


def load(path: str | pathlib.Path):
    """
    Load (deserialize) a Sudoku puzzle.

    Supports *.msk, *.sol, and *.ss formats.
    """
    path = pathlib.Path(path)
    assert path.exists()

    with open(path) as stream:
        sequence = re.findall(r"[123456789.]", stream.read())

    if (actual := len(sequence)) != 81:
        raise ValueError(f"Expect 81 values in {path}, got {actual}")
    puzzle = SudokuBoard.from_sequence(sequence)
    return puzzle


def dump(puzzle: SudokuBoard, filename: str | pathlib.Path):
    """Dump (serialize) a Sudoku puzzle in *.ss format."""
    path = pathlib.Path(filename)
    if path.suffix != ".ss":
        raise ValueError(f"Expect filename which ends with .ss, not {filename}")

    text = puzzle.to_string(ascii=True)
    path.write_text(text + "\n")
