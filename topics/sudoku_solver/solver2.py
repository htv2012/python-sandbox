#!/usr/bin/env python3
"""
A sudoku solver
"""
import collections
import collections.abc
import io
import itertools


ROWS = "ABCDEFGHI"
COLS = list(range(9))
EMPTY = "."

class Sudoku(collections.abc.MutableMapping):

    def __init__(self, grid=None):
        if grid is None:
            return

        coords = itertools.product(ROWS, COLS)
        values = grid.split()
        self.grid = {}

        for coord, value in zip(coords, values):
            self.grid[coord] = value

    def __delitem__(self, key):
        pass

    def __getitem__(self, key):
        row, col = key
        row = row.upper()
        return self.grid[row, col]

    def __iter__(self, key):
        pass

    def __len__(self):
        pass

    def __setitem__(self):
        pass

    def __str__(self):
        buf = io.StringIO()
        for index, cell in enumerate(self.grid.values()):
            buf.write(cell)
            buf.write(" ")
            col = index % 9
            if col == 2 or col == 5:
                buf.write("| ")
            elif col == 8:
                buf.write("\n")
            if index == 26 or index == 53:
                buf.write("------+-------+-------\n")
        return buf.getvalue()

    def candidates(self, row, col):
        if self.grid[row, col] != EMPTY:
            return [self.grid[row, col]]

        available = set("0123456789")
        for other_col in COLS:
            available.discard(self.grid[row, other_col])
        for other_row in ROWS:
            available.discard(self.grid[other_row, col])


my_grid = """
. 2 . 4 9 . 8 7 .
4 1 . . 7 . 6 . .
8 5 7 . 6 3 . . 1
. . . 8 . . . . .
. 8 . . 5 . . 9 .
. . . . . 2 . . .
5 . . 9 1 . 7 3 2
. . 2 . 8 . . 6 9
. 4 3 . 2 7 . 1 .
"""


def main():
    """ Entry """
    sudoku = Sudoku(my_grid)
    print(sudoku)
    for 


if __name__ == '__main__':
    main()

