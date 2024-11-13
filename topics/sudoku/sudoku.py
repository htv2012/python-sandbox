import io
import pprint


EMPTY = "."
DIGITS = "123456789"
b = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

b = [
    [".", "2", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "6", ".", ".", ".", ".", "3"],
    [".", "7", "4", ".", "8", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "2"],
    [".", "8", ".", ".", "4", ".", ".", "1", "."],
    ["6", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", "1", ".", "7", "8", "."],
    ["5", ".", ".", ".", ".", "9", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "4", "."],
]


def to_string(board):
    buf = io.StringIO()
    for row in range(9):
        for col in range(9):
            buf.write(f" {board[row][col]}")
            if col in {2, 5}:
                buf.write(" |")
        buf.write("\n")
        if row in {2, 5}:
            buf.write("-------|-------|-------\n")
    return buf.getvalue()


def print_board(board):
    print(to_string(board))


def neighbors(row, col):
    for row2 in range(9):
        if row2 != row:
            yield row2, col

    for col2 in range(9):
        if col2 != col:
            yield row, col2

    base_row = row // 3 * 3
    base_col = col // 3 * 3
    for row_offset in range(3):
        row2 = base_row + row_offset
        for col_offset in range(3):
            col2 = base_col + col_offset
            if (row2, col2) != (row, col):
                yield row2, col2


def conflicted(board, row, col, candidate):
    for r, c in neighbors(row, col):
        if board[r][c] == candidate:
            return True
    return False


def solve(board) -> bool:
    for row in range(9):
        for col in range(9):
            if board[row][col] != EMPTY:
                continue
            for candidate in DIGITS:
                if conflicted(board, row, col, candidate):
                    continue
                board[row][col] = candidate
                if solve(board):
                    return True
                board[row][col] = EMPTY
            # None of the candidates fits, puzzle is not solvable
            return False
    # No more empty cells: solved
    return True


print_board(b)
pprint.pprint(b)
solved = solve(b)
print(f"{solved=}")
print_board(b)
