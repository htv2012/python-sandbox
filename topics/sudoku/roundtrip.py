"""
Round trip conversion: load, dump
"""

import sudoku


def main():
    puzzle1 = sudoku.load("puzzle1.ss")
    sudoku.dump(puzzle1, "out.ss")


if __name__ == "__main__":
    main()
