import sudoku


def main():
    sud = sudoku.load("puzzle1.msk")
    print(sud)
    if sud.solve():
        print(sud)


if __name__ == "__main__":
    main()
