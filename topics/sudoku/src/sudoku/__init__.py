import collections
import io
import itertools
import logging
import pathlib
import re

logger = logging.getLogger()

EMPTY_CELL = "."
ROW_INDICES = list(range(9))
COL_INDICES = list(range(9))
ALL_INDICES = list(itertools.product(ROW_INDICES, COL_INDICES))


class SudokuBoard:
    def __init__(self):
        self.board = collections.defaultdict(lambda: EMPTY_CELL)
        self.original = {}

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
        for row, col in ALL_INDICES:
            if self.board[row, col] != EMPTY_CELL:
                continue
            for candidate in "123456789":
                if self.conflicted(row, col, candidate):
                    continue
                self.board[row, col] = candidate
                if self.solve():
                    return True
            self.board[row, col] = EMPTY_CELL
            return False
        return True

    def conflicted(self, row, col, candidate) -> bool:
        """Does this candidate causes a conflict?"""
        return any(
            self.board[row2, col2] == candidate
            for row2, col2 in self.neighbors(row, col)
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

    def mark_original(self):
        self.original = dict(self.board)

    @property
    def original_in_tact(self) -> bool:
        diff = [
            (row, col)
            for row, col in ALL_INDICES
            if not (
                self.original[row, col] == EMPTY_CELL
                or self.board[row, col] == self.original[row, col]
            )
        ]
        if diff:
            for row, col in diff:
                logger.debug(
                    f"diff: {self.board[row, col]=}, {self.original[row, col]=}"
                )
        return not diff

    @property
    def is_valid(self):
        return all(
            self.board[row, col] == EMPTY_CELL
            or not self.conflicted(row, col, self.board[row, col])
            for row, col in ALL_INDICES
        )

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

    text = str(puzzle)
    replacement_table = [
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
    for old, new in replacement_table:
        text = text.replace(old, new)
    path.write_text(text + "\n")
