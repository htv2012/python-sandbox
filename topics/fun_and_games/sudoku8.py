
EMPTY = '.'
ROWS = 'ABCDEFGHI'
COLUMNS = range(9)
COORDINATES = [(row, column) for row in ROWS for column in COLUMNS]


def box_normalize(row, column):
    column = column // 3 * 3
    row_index = ROWS.index(row)
    row_index = row_index // 3 * 3
    row = ROWS[row_index]
    return row, column


def same_box(row1, column1, row2, column2):
    return box_normalize(row1, column1) == box_normalize(row2, column2)


def next_unsolved_coordinate(grid):
    unsolved_coordinates = (coordinate for coordinate in COORDINATES if grid[coordinate] == EMPTY)
    return next(unsolved_coordinates, None)


def find_candidates(grid, here_row, here_column):
    candidates = set('123456789')
    non_candidates = set(
        (row, column)
        for row, column in COORDINATES
        if row == here_row or column == here_column or same_box(row, column, here_row, here_column))
    candidates -= non_candidates
    return candidates


def solve(grid):
    """
    Attempts to solve the sudoku grid, return True if it can solve it, False if
    not.
    """
    coordinate = next_unsolved_coordinate(grid)
    if coordinate is None:
        return True

    candidates = find_candidates(grid, *coordinate)
    for candidate in candidates:
        grid[coordinate] = candidate
        if solve(grid):
            return True

    grid[coordinate] = EMPTY
    return False


grid = dict.fromkeys(COORDINATES, '.')
solved = solve(grid)
if solved:
    print('Solved')
else:
    print('Not solved')
