import sudoku


def main():
    puzzle = sudoku.load("puzzle1.ss")
    print(puzzle)
    if puzzle.solve():
        print(puzzle)


if __name__ == "__main__":
    main()
