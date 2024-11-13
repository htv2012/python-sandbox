"""
Solve sudoku
"""
import io
import re


EMPTY = '.'
rows = 'ABCDEFGHI'
columns = range(9)
all_coordinates = [(row, column) for row in rows for column in columns]


def nw_corner(coordinate):
    row, column = coordinate
    nw_row = rows[rows.index(row) // 3 * 3]
    nw_column = column // 3 * 3
    return nw_row, nw_column


def same_box(coordinate1, coordinate2):
    return nw_corner(coordinate1) == nw_corner(coordinate2)


def generate_neighbors_table():
    table = {}
    for coordinate in all_coordinates:
        table[coordinate] = set(
            c for c in all_coordinates
            if coordinate[0] == c[0] or coordinate[1] == c[1] or same_box(coordinate, c))
    return table


neighbors = generate_neighbors_table()


class Sudoku:
    def __init__(self):
        self.load(EMPTY * 81)

    def load(self, values):
        self.grid = dict(zip(all_coordinates, values))

    def load_simple(self, data):
        self.load(re.findall(r'[123456789.]', data))

    def __str__(self):
        buffer = io.StringIO()
        buffer.write('   0  1  2   3  4  5   6  7  8\n')
        for row in rows:
            if row in 'ADG':
                buffer.write(' |---------|---------|---------|\n')
            buffer.write('{}| {}  {}  {} | {}  {}  {} | {}  {}  {} |\n'.format(row, *[self.grid[row, c] for c in columns]))

        buffer.write(' |---------|---------|---------|\n')
        return buffer.getvalue()

    def next_unsolved_coordinate(self):
        return next((coordinate for coordinate in all_coordinates if self.grid[coordinate] == EMPTY), None)

    def find_candidates(self, coordinate):
        all_candidates = set('123456789')
        non_candidates = set(self.grid[c] for c in neighbors[coordinate])
        candidates = all_candidates - non_candidates
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


if __name__ == '__main__':
    s = Sudoku()
    print(s)

    s.load_simple("""
    .7..3.89.
    .9.....23
    5....6...
    .4.6.7..8
    .........
    3..2.9.4.
    ...7....1
    42.....6.
    .18.6..7.
    """)
    print(s)

    solved = s.solve()
    print(s)
    print({True: 'Solved', False: 'Not solved'}[solved])
