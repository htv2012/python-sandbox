"""
Solve sudoku
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


def calculate_neighbors_table():
    table = {}
    for here_row, here_column in all_coordinates:
        table[here_row, here_column] = set(
            (row, column)
            for row, column in all_coordinates
            if row == here_row or column == here_column or same_box(row, column, here_row, here_column)
        )
        table[here_row, here_column].discard((here_row, here_column))
    return table


neighbors = calculate_neighbors_table()


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
        return next ((coordinate for coordinate, cell in self.grid.items() if cell == EMPTY), None)

    def calculate_candidates(self, coordinate):
        candidates = set('123456789')
        non_candidates = set(self.grid[c] for c in neighbors[coordinate])
        return candidates - non_candidates

    def solve(self):
        coordinate = self.next_unsolved_coordinate()
        if coordinate is None:
            return True

        candidates = self.calculate_candidates(coordinate)
        for candidate in candidates:
            self.grid[coordinate] = candidate
            if self.solve():
                return True

        self.grid[coordinate] = EMPTY
        return False


sudoku = Sudoku.from_output("""
   0  1  2   3  4  5   6  7  8
 |---------|---------|---------|
A| .  7  . | .  2  . | 5  1  . |
B| .  .  . | .  .  . | .  .  2 |
C| .  6  . | .  .  . | 3  .  7 |
 |---------|---------|---------|
D| 5  .  . | .  7  . | .  4  . |
E| .  .  9 | .  .  . | 2  .  5 |
F| 8  .  . | 5  .  . | 6  .  . |
 |---------|---------|---------|
G| .  1  . | 3  9  6 | .  .  . |
H| .  .  . | .  .  . | .  .  . |
I| 7  .  . | .  .  . | .  .  9 |
 |---------|---------|---------|
""")
print(sudoku)
solved = sudoku.solve()
print(sudoku)
print({True: 'Solved', False: 'Not solved'}[solved])
