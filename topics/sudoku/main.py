import sudoku

sud = sudoku.load("puzzle1.ss")
print(sud)
if sud.solve():
    print(sud)
