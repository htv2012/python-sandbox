from collections import defaultdict

COLS = "ABCDEFGHIJ"
ROWS = "1234567890"

MARK_EMPTY = " "
MARK_HIT = "x"
MARK_MISS = "."
MARK_SUNK = "X"


class ShipBoard:
    def __init__(self):
        self.grid = defaultdict(lambda: MARK_EMPTY)
        self.health = {}
        self.ship = {}
        self.ids = iter(range(5))

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
