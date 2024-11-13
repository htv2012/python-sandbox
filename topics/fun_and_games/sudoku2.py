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


# for c in [('D', 2), ('D', 3), ('E', 4), ('F', 5)]:
#     print(c, nw_corner(c))
# raise SystemExit(1)


def same_block(coordinate1, coordinate2):
    return nw_corner(coordinate1) == nw_corner(coordinate2)


def generate_neighbors():
    neighbors = {}
    for row, column in all_coordinates:
        neighbors[row, column] = [(r, c) for r, c in all_coordinates if row == r or column == c or same_block((row, column), (r, c))]
        neighbors[row, column].remove((row, column))

    return neighbors


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
        return next((coordinate for coordinate, cell in self.grid.items() if cell == EMPTY), None)

    def find_candidates(self, coordinate):
        candidates = set('123456789')
        for neighbor in neighbors[coordinate]:
            candidates.discard(self.grid[neighbor])
        return candidates

    def solve_by_brute_force(self):
        coordinate = self.next_unsolved_coordinate()
        if coordinate is None:
            return True  # No more unsolved

        candidates = self.find_candidates(coordinate)
        for candidate in candidates:
            self.grid[coordinate] = candidate
            if self.solve_by_brute_force():
                return True

        # Gets here mean none of the candidate offer a solution, back track
        self.grid[coordinate] = EMPTY
        return False


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