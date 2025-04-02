import io
from collections import defaultdict

COLS = "ABCDEFGHIJ"
ROWS = "1234567890"
IDS = "01234"

MARK_EMPTY = " "
MARK_HIT = "x"
MARK_MISS = "."
MARK_SUNK = "X"


class ShipBoard:
    def __init__(self):
        self.grid = defaultdict(lambda: MARK_EMPTY)
        self.health = {}
        self.ship = {}
        self.ids = iter(IDS)

    def add(self, *ship):
        # TODO: Validate each coordinate, flag such coordinate as A13, or X2
        # TODO: Validate adding ship to empty spaces
        ship_id = next(self.ids)
        for coord in ship:
            self.grid[coord] = ship_id
        self.ship[ship_id] = tuple(ship)
        self.health[ship_id] = len(ship)

    def assess(self, coord: str):
        if self.grid[coord] == MARK_EMPTY:
            self.grid[coord] = MARK_MISS
        if self.grid[coord] in {MARK_HIT, MARK_MISS, MARK_SUNK}:
            return self.grid[coord]

        ship_id = self.grid[coord]
        self.health[ship_id] -= 1
        self.grid[coord] = MARK_SUNK if self.health[ship_id] == 0 else MARK_HIT
        return self.grid[coord]

    def __str__(self):
        buf = io.StringIO()
        buf.write("SHIPS\n\n")
        buf.write("  │ A │ B │ C │ D │ E │ F │ G │ H │ I │ J │\n")
        buf.write("──┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───│\n")

        for row in ROWS:
            buf.write(f"{row} │")
            for col in COLS:
                buf.write(f" {self.grid[col + row]} │")
            buf.write("\n")
            if row == "0":
                buf.write("──┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘\n")
            else:
                buf.write("──┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───│\n")

        return buf.getvalue()
