import random

from .const import ALL_COORDINATES, COLS, ROWS, normalize_coordinate
from .logger import logger
from .ship_board import ShipBoard
from .target_board import TargetBoard


class Player:
    def __init__(self, name: str = None):
        self.name = name
        self.ship_board = ShipBoard()
        self.target_board = TargetBoard()

    def generate_ship(self, ship_id, ship_size) -> list[str]:
        raise NotImplementedError("generate_ship")

    def add_ships(self):
        occupied = set()
        for ship_id, ship_size in enumerate([3, 3, 4, 5, 2]):
            conflicted = True
            while conflicted:
                ship = self.generate_ship(ship_id, ship_size)
                conflicted = any(c in occupied for c in ship)

                logger.debug("occupied: %r", occupied)
                logger.debug("ship ID: %d, ship: %r", ship_id, ship)
                logger.debug("conflicted: %r", conflicted)

            self.ship_board.add(*ship)
            occupied.update(ship)

    @property
    def is_lost(self) -> bool:
        return self.ship_board.all_sunk

    def assess(self, coord):
        return self.ship_board.assess(coord)

    def move(self):
        raise NotImplementedError()

    def mark(self, coord, result):
        """Mark the target board."""
        raise NotImplementedError("mark")


class HumanPlayer(Player):
    def generate_ship(self, ship_id, ship_size) -> list[str]:
        valid = False
        while not valid:
            ship = input(f"Ship #{ship_id} (size={ship_size}): ").upper().split()
            ship = [normalize_coordinate(c) for c in ship]
            valid = (len(ship) == ship_size) and all(c in ALL_COORDINATES for c in ship)
        return ship

    def move(self):
        pass

    def mark(self, coord, result):
        """Mark the target board."""
        self.target_board.mark(coord, result)


class ComputerPlayer(Player):
    def move(self):
        pass

    def generate_ship(self, ship_id, ship_size) -> list[str]:
        direction = random.choice(["vertical", "horizontal"])
        if direction == "vertical":
            row_index = random.randint(0, len(ROWS) - ship_size)
            col_index = random.randint(0, len(COLS) - 1)
            ship = [ROWS[row_index + i] + COLS[col_index] for i in range(ship_size)]
        else:
            row_index = random.randint(0, len(ROWS) - 1)
            col_index = random.randint(0, len(COLS) - ship_size)
            ship = [ROWS[row_index] + COLS[col_index + i] for i in range(ship_size)]
        return ship
