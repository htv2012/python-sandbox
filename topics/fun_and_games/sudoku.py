#!/usr/bin/env python3
"""
Solve a Sudoku puzzle
"""
import logging
import os
from io import StringIO


logging.basicConfig(level=os.getenv("LOGLEVEL", logging.INFO))
logger = logging.getLogger(__name__)


class SudokuBoard:
    def __init__(self):
        self.rows = 'ABCDEFGHI'
        self.columns = range(9)
        self.all_coordinates = [(r, c) for r in self.rows for c in self.columns]
        self.load('.' * 81)

    def load(self, data):
        data =''.join(row.strip() for row in data.splitlines())
        self.grid = dict(zip(self.all_coordinates, data))

    def nw_corner_of_block(self, coordinate):
        row, column = coordinate
        column = column // 3 * 3
        row = self.rows[self.rows.index(row) // 3 * 3]
        return row, column

    def same_block(self, coordinate1, coordinate2):
        nw1 = self.nw_corner_of_block(coordinate1)
        nw2 = self.nw_corner_of_block(coordinate2)
        return nw1 == nw2

    def neighbors(self, coordinate):
        """
        Returns the neighboring coordinates
        """
        row, column = coordinate
        result = [cell for cell in self.all_coordinates
            if (row in cell) or (column in cell) or self.same_block(coordinate, cell)]
        result.remove(coordinate)
        return result

    def __str__(self):
        buffer = StringIO()
        buffer.write('   0  1  2   3  4  5   6  7  8\n')
        for row in self.rows:
            if row in {'A', 'D', 'G'}:
                buffer.write(' |---------|---------|---------|\n')

            data = [self.grid[row, column] for column in self.columns]
            buffer.write('{}| {}  {}  {} | {}  {}  {} | {}  {}  {} |\n'.format(row, *data))
        buffer.write(' |---------|---------|---------|\n')
        return buffer.getvalue()

    def find_possibilities(self, coordinate):
        possibilities = set('123456789')

        for neighbor_coordinate in self.neighbors(coordinate):
            possibilities.discard(self.grid[neighbor_coordinate])

        return possibilities

    def solve_by_elimination(self):
        changed = True
        while changed:
            changed = False
            for coordinate in self.all_coordinates:
                if self.grid[coordinate] == '.':
                    possibilities = self.find_possibilities(coordinate)
                    if len(possibilities) == 1:
                        changed = True
                        cell = possibilities.pop()
                        logger.debug('Cell %s ==> %s', coordinate, cell)
                        self.grid[coordinate] = cell

    def next_unsolved_coordinate(self):
        return next((coordinate for coordinate, cell in self.grid.items() if cell == '.'), None)

    def solve_by_brute_force(self):
        """
        Solve by trying all possibilities until one works
        """
        coordinate = self.next_unsolved_coordinate()
        if coordinate is None:
            return True  # All solved

        possibilities = self.find_possibilities(coordinate)
        if not possibilities:
            return False  # Dead end: wrong choice in prior move(s)

        for possibility in possibilities:
            self.grid[coordinate] = possibility
            if self.solve_by_brute_force():
                return True

        # None of the possibilities works, we have made one or more wrong
        # choices in prior move(s)
        self.grid[coordinate] = '.'
        return False

    @property
    def solved(self):
        return '.' not in self.grid.values()

b = SudokuBoard()
b.load("""
....5..7.
.74......
5..29...1
86...41..
..3.6.9..
..93...26
7...31..4
......58.
.4..8....
""")
b.load("""
..95.2..8
.5.1..3.2
4....3...
.9......7
.6.....2.
1......9.
...2....3
5.6..7.4.
7..8.45..
""")
print(b)
b.solve_by_elimination()
print(b)
print('Solved?', b.solved)

b.solve_by_brute_force()
print(b)
print('Solved?', b.solved)
