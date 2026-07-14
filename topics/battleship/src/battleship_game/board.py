import io

from . import const


class Board:
    _board_title = ""

    def __init__(self):
        self.grid = dict.fromkeys(const.ALL_COORDINATES, const.MARK_EMPTY)
        self.shots_count = 0

    @property
    def hits_count(self) -> int:
        hits = [
            mark
            for mark in self.grid.values()
            if mark in {const.MARK_HIT, const.MARK_SUNK}
        ]
        return len(hits)

    @property
    def sunks_count(self) -> int:
        hits = [mark for mark in self.grid.values() if mark == const.MARK_SUNK]
        return len(hits)

    def __str__(self):
        buf = io.StringIO()
        buf.write(self._board_title.ljust(const.BOARD_WIDTH))
        buf.write("\n\n")
        buf.write("  │ A │ B │ C │ D │ E │ F │ G │ H │ I │ J │\n")
        buf.write("──┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───│\n")

        for row in const.ROWS:
            buf.write(f"{row} │")
            for col in const.COLS:
                buf.write(f" {self.grid[row + col]} │")
            buf.write("\n")
            if row == const.ROWS[-1]:
                buf.write("──┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘\n")
            else:
                buf.write("──┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───│\n")

        status = f"Shots: {self.shots_count} | Hits: {self.hits_count} | Sunks: {self.sunks_count}"
        buf.write(status.ljust(const.BOARD_WIDTH))
        buf.write("\n")

        return buf.getvalue()


class ShipBoard(Board):
    _board_title = "OUR SHIPS"

    def __init__(self):
        super().__init__()
        self.health = {}  # {ship_id: int}

    def add(self, ship_id, ship):
        for coord in ship:
            coord = const.normalize_coordinate(coord)
            self.grid[coord] = ship_id
        self.health[ship_id] = len(ship)

    def report(self, coord: str):
        self.shots_count += 1
        if self.grid[coord] == const.MARK_EMPTY:
            self.grid[coord] = const.MARK_MISS
        # if self.grid[coord] not in {const.MARK_HIT, const.MARK_MISS, const.MARK_SUNK}:
        elif self.grid[coord] in const.SHIP_IDS:
            ship_id = self.grid[coord]
            self.health[ship_id] -= 1
            self.grid[coord] = (
                const.MARK_SUNK if self.health[ship_id] == 0 else const.MARK_HIT
            )
        return self.grid[coord]

    @property
    def all_sunk(self):
        return sum(self.health.values()) == 0


class TargetBoard(Board):
    _board_title = "OPPONENT'S SHIPS"

    def mark(self, coord, result):
        coord = const.normalize_coordinate(coord)
        if coord not in self.grid:
            raise ValueError(f"Invalid coordinate: {coord}")
        self.grid[coord] = result
        self.shots_count += 1
