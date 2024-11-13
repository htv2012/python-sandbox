"""
Solve sudoku
"""
import re


EMPTY = '.'
ROWS = 'ABCDEFGHI'
COLUMNS = range(9)
COORDINATES = [(r, c) for r in ROWS for c in COLUMNS]


def nw_corner(row, column):
    row = ROWS[ROWS.index(row) // 3 * 3]
    column = column // 3 * 3
    return row, column


def same_block(row1, column1, row2, column2):
    return nw_corner(row1, column1) == nw_corner(row2, column2)


def calculate_neighbors():
    table = {}
    for here_row, here_column in COORDINATES:
        table[here_row, here_column] = set(
            (row, column)
            for row, column in COORDINATES
            if here_row == row or here_column == column or same_block(here_row, here_column, row, column)
        )

        table[here_row, here_column].discard((here_row, here_column))

    return table


neighbors = calculate_neighbors()


def load_grid(data):
    cells = re.findall(r'[1-9.]', data)
    grid = dict(zip(COORDINATES, cells))
    return grid


def print_grid(grid):
    print('   0  1  2   3  4  5   6  7  8')
    print(' |---------|---------|---------|')
    for row in ROWS:
        print(' | {}  {}  {} | {}  {}  {} | {}  {}  {} |'.format(*[grid[row, column] for column in COLUMNS]))
        if row in 'CFI':
            print(' |---------|---------|---------|')


def next_unsolved_coordinate(grid):
    return next((coordinate for coordinate in COORDINATES if grid[coordinate] == EMPTY), None)


def find_candidates(grid, coordinate):
    candidates = set('123456789')
    non_candidates = set(grid[c] for c in neighbors[coordinate])
    candidates -= non_candidates
    return candidates


def solve(grid):
    coordinate = next_unsolved_coordinate(grid)
    if coordinate is None:
        return True

    candidates = find_candidates(grid, coordinate)
    for candidate in candidates:
        grid[coordinate] = candidate
        if solve(grid):
            return True

    # None of the candidates provide a solution, back track
    grid[coordinate] = EMPTY
    return False


if __name__ == '__main__':
    grid = load_grid("""
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
    print_grid(grid)

    solved = solve(grid)

    print_grid(grid)
    if solved:
        print('Solved')
    else:
        print('Not solved')
