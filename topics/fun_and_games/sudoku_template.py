"""
Solve the sudoku
"""
import io
import logging
import os
import re


logging.basicConfig(level=os.getenv('LOGLEVEL', logging.INFO))
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


EMPTY = '.'
rows = 'ABCDEFGHI'
columns = range(9)
all_coordinates = [(r, c) for r in rows for c in columns]


def nw_corner(coordinate):
    row, column = coordinate
    row = rows[rows.index(row) // 3 * 3]
    column = column // 3 * 3
    return row, column


def same_block(coordinate1, coordinate2):
    return nw_corner(coordinate1) == nw_corner(coordinate2)


def generate_neighbors():
    table = {}
    for row, column in all_coordinates:
        table[row, column] = [(r, c) for r, c in all_coordinates if row == r or column == c or same_block((row, column), (r, c))]
        table[row, column].remove((row, column))

    return table


neighbors = generate_neighbors()


class Sudoku:
    def __init__(self):
        self.load(EMPTY * 81)

    def load(self, values):
        self.grid = dict(zip(all_coordinates, values))

    def __str__(self):
        buffer = io.StringIO()
        buffer.write('   0  1  2   3  4  5   6  7  8\n')
        for row in rows:
            if row in 'ADG':
                buffer.write(' |---------|---------|---------|\n')
            buffer.write('{}| {}  {}  {} | {}  {}  {} | {}  {}  {} |\n'.format(row, *[self.grid[row, c] for c in columns]))

        buffer.write(' |---------|---------|---------|\n')
        return buffer.getvalue()

    @classmethod
    def from_output(cls, output):
        # Remove the header
        output = output.replace('0  1  2   3  4  5   6  7  8', '')

        # Extract all digits and dot (which represents the blank)
        cells = re.findall(r'[123456789.]', output)

        board = cls()
        board.load(cells)
        return board

    def next_unsolved_coordinate(self):
        pass

    def find_candidates(self, coordinate):
        pass

    def solve_by_brute_force(self):
        pass


sudoku = Sudoku.from_output("""
   0  1  2   3  4  5   6  7  8
 |---------|---------|---------|
A| .  .  9 | 5  .  2 | .  .  8 |
B| .  5  . | 1  .  . | 3  .  2 |
C| 4  .  . | .  .  3 | .  .  . |
 |---------|---------|---------|
D| .  9  . | .  .  . | .  .  7 |
E| .  6  . | .  .  . | .  2  . |
F| 1  .  . | .  .  . | .  9  . |
 |---------|---------|---------|
G| .  .  . | 2  .  . | .  .  3 |
H| 5  .  6 | .  .  7 | .  4  . |
I| 7  .  . | 8  .  4 | 5  .  . |
 |---------|---------|---------|
""")
print(sudoku)
# print(sudoku.find_candidates(('A', 0)))
sudoku.solve_by_brute_force()
print(sudoku)