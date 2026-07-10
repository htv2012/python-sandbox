# test_original.py
import sudoku


def test_in_tact(puzzle):
    """Verify original in tact"""
    assert puzzle.original_in_tact

    # Alter empty cells
    for row, col in puzzle.board:
        if puzzle.board[row, col] == sudoku.EMPTY_CELL:
            puzzle.board[row, col] = "9"

    assert puzzle.original_in_tact


def test_not_in_tact(puzzle):
    """Alter 3 cells and verify original not in tact."""
    counter = 0
    for coord in puzzle.board:
        if puzzle.board[coord] != sudoku.EMPTY_CELL:
            puzzle.board[coord] = str(10 - int(puzzle.board[coord]))
            counter += 1
        if counter >= 3:
            break

    assert not puzzle.original_in_tact
