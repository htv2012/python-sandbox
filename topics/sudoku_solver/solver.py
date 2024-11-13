import sudoku

my_grid = """
. 2 . 4 9 . 8 7 .
4 1 . . 7 . 6 . .
8 5 7 . 6 3 . . 1
. . . 8 . . . . .
. 8 . . 5 . . 9 .
. . . . . 2 . . .
5 . . 9 1 . 7 3 2
. . 2 . 8 . . 6 9
. 4 3 . 2 7 . 1 .
""".strip().splitlines()


def main():
    board = sudoku.Board()
    board.read(my_grid)
    print(board)


if __name__ == '__main__':
    main()
