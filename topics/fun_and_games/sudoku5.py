"""
Solve the sudoku
"""
import io
import re

EMPTY = '.'
rows = 'ABCDEFGHI'
columns = range(9)
all_coordinates = [(row, column) for row in rows for column in columns]


def nw_corner(row, column):
    row = rows[rows.index(row) // 3 * 3]
    column = column // 3 * 3
    return row, column


def same_box(row1, column1, row2, column2):
    return nw_corner(row1, column1) == nw_corner(row2, column2)


def calculate_neighbors():
    table = {}
    for here in all_coordinates:
        here_row, here_column = here
        table[here_row, here_column] = set(
            (r, c)
            for r, c in all_coordinates
            if here_row == r or here_column == c or same_box(here_row, here_column, r, c)
        )

    return table


neighbors = calculate_neighbors()



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
        return next((coordinate for coordinate in all_coordinates if self.grid[coordinate] == EMPTY), None)

    def find_candidates(self, coordinate):
        candidates = set('123456789')
        non_candidates = set(self.grid[c] for c in neighbors[coordinate])
        candidates -= non_candidates
        return candidates

    def solve(self):
        coordinate = self.next_unsolved_coordinate()
        if coordinate is None:
            return True

        candidates = self.find_candidates(coordinate)
        for candidate in candidates:
            self.grid[coordinate] = candidate
            if self.solve():
                return True

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
solved = sudoku.solve()
print(sudoku)
print({True: 'Solved', False: 'Not solved'}[solved])
