import itertools

ROWS = "ABCDEFGHIJ"
COLS = "1234567890"

ALL_COORDINATES = ["%s%s" % (coord) for coord in itertools.product(ROWS, COLS)]
IDS = "01234"

MARK_EMPTY = " "
MARK_HIT = "x"
MARK_MISS = "."
MARK_SUNK = "X"

BOARD_WIDTH = 43
