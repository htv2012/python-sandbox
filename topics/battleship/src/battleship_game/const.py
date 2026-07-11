import itertools

COLS = "ABCDEFGHIJ"
ROWS = "1234567890"

ALL_COORDINATES = ["%s%s" % (coord) for coord in itertools.product(ROWS, COLS)]
IDS = "01234"

MARK_EMPTY = " "
MARK_HIT = "x"
MARK_MISS = "."
MARK_SUNK = "X"

BOARD_WIDTH = 43


def normalize_coordinate(coord: str):
    if coord in ALL_COORDINATES:
        return coord

    swapped_order = coord[1] + coord[0]
    if swapped_order not in ALL_COORDINATES:
        raise ValueError(f"Not a valid coordinate: {coord}")
    return swapped_order
