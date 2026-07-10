import argparse

import sudoku


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    options = parser.parse_args()

    puzzle = sudoku.load(options.filename)
    print(puzzle)
    if puzzle.solve():
        print(puzzle)
    else:
        print("Not solvable")


if __name__ == "__main__":
    main()
