import itertools

# coordinates
COLS = "ABCDEFGHIJ"
ROWS = "1234567890"
ALL_COORDINATES = ["%s%s" % (coord) for coord in itertools.product(ROWS, COLS)]

# ship
SHIP_IDS = "01234"
SHIP_SIZES = [3, 3, 4, 5, 2]
SHIP_MAX_HEALTH = sum(SHIP_SIZES)

MARK_EMPTY = " "
MARK_HIT = "x"
MARK_MISS = "."
MARK_SUNK = "X"

BOARD_WIDTH = 43
BOARD_GAP = 8


def normalize_coordinate(coord: str):
    if coord in ALL_COORDINATES:
        return coord

    swapped_order = coord[1] + coord[0]
    return swapped_order
