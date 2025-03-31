import sudoku

sud = sudoku.load("puzzle1.msk")
print(sud)
if sud.solve():
    print(sud)
