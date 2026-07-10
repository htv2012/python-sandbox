"""
Round trip conversion: load, dump
"""

import sudoku


def main():
    puzzle = sudoku.load("puzzle1.ss")
    sudoku.dump(puzzle, "out.ss")
    puzzle.solve()
    sudoku.dump(puzzle, "solved.ss")


if __name__ == "__main__":
    main()
