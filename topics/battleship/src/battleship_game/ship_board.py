from . import Board, const


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
        if self.grid[coord] in {const.MARK_HIT, const.MARK_MISS, const.MARK_SUNK}:
            return self.grid[coord]

        ship_id = self.grid[coord]
        self.health[ship_id] -= 1
        self.grid[coord] = (
            const.MARK_SUNK if self.health[ship_id] == 0 else const.MARK_HIT
        )
        return self.grid[coord]

    @property
    def all_sunk(self):
        return sum(self.health.values()) == 0
