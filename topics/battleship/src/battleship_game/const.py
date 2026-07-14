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
MARK_HIT = "\u25cf"
MARK_MISS = "\u25cb"
MARK_SUNK = "\u26ec"

BOARD_WIDTH = 43
BOARD_GAP = 8


def normalize_coordinate(coord: str):
    coord = coord.upper()
    if coord in ALL_COORDINATES:
        return coord

    try:
        swapped_order = coord[1] + coord[0]
        return swapped_order
    except (ValueError, IndexError):
        # too many chars and too few chars, respectively
        return coord
