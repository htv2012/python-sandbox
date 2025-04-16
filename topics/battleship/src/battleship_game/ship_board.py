import io
from collections import defaultdict

from . import const


class ShipBoard:
    def __init__(self):
        self.grid = defaultdict(lambda: const.MARK_EMPTY)
        self.health = {}
        self.ship = {}
        self.ids = iter(const.IDS)
        self.shots_count = 0

    def add(self, *ship):
        # TODO: Validate each coordinate, flag such coordinate as A13, or X2
        # TODO: Validate adding ship to empty spaces
        ship_id = next(self.ids)
        for coord in ship:
            self.grid[coord] = ship_id
        self.ship[ship_id] = tuple(ship)
        self.health[ship_id] = len(ship)

    def assess(self, coord: str):
        self.shots_count += 1
        if self.grid[coord] == const.MARK_EMPTY:
            self.grid[coord] = const.MARK_MISS
        if self.grid[coord] in {const.MARK_HIT, const.MARK_MISS, const.MARK_SUNK}:
            return self.grid[coord]

        ship_id = self.grid[coord]
        self.health[ship_id] -= 1
        self.grid[coord] = (
            const.MARK_SUNK if self.health[ship_id] == 0 else const.MARK_HIT
        )
        return self.grid[coord]

    def __str__(self):
        buf = io.StringIO()
        buf.write("SHIPS".ljust(const.BOARD_WIDTH))
        buf.write("\n\n")
        buf.write("  │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │ 0 │\n")
        buf.write("──┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───│\n")

        for row in const.ROWS:
            buf.write(f"{row} │")
            for col in const.COLS:
                buf.write(f" {self.grid[row + col]} │")
            buf.write("\n")
            if row == "J":
                buf.write("──┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘\n")
            else:
                buf.write("──┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───│\n")

        shots_fired = f"{self.shots_count} shot(s) fired"
        buf.write(shots_fired.ljust(const.BOARD_WIDTH))
        buf.write("\n")

        return buf.getvalue()
