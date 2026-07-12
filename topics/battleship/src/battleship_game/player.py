import contextlib
import random

from .const import ALL_COORDINATES, COLS, ROWS, iter_ships, normalize_coordinate
from .logger import logger
from .ship_board import ShipBoard
from .target_board import TargetBoard


class Player:
    def __init__(self):
        self.ship_board = ShipBoard()
        self.target_board = TargetBoard()
        self.available_coordinates = set(ALL_COORDINATES)

    def generate_ship(self, ship_id, ship_size) -> list[str]:
        raise NotImplementedError("generate_ship")

    def add_ships(self):
        occupied = set()
        for ship_id, ship_size in iter_ships():
            conflicted = True
            while conflicted:
                ship = self.generate_ship(ship_id, ship_size)
                conflicted = any(c in occupied for c in ship)

                logger.debug("occupied: %r", occupied)
                logger.debug("ship ID: %r, ship: %r", ship_id, ship)
                logger.debug("conflicted: %r", conflicted)

            self.ship_board.add(ship_id, ship)
            occupied.update(ship)

    @property
    def is_lost(self) -> bool:
        return self.ship_board.all_sunk

    def assess(self, coord):
        return self.ship_board.assess(coord)

    def fire(self):
        raise NotImplementedError("fire")

    def mark(self, coord, result):
        """Mark the target board."""
        self.target_board.mark(coord, result)


class HumanPlayer(Player):
    def generate_ship(self, ship_id, ship_size) -> list[str]:
        print(self.ship_board)
        valid = False
        while not valid:
            ship = input(f"Ship #{ship_id} (size={ship_size}): ").upper().split()
            ship = [normalize_coordinate(c) for c in ship]
            valid = (len(set(ship)) == ship_size) and all(
                c in ALL_COORDINATES for c in ship
            )
        return ship

    def fire(self):
        coord = None
        while coord not in self.available_coordinates:
            coord = input("Coordinate: ").upper()
            with contextlib.suppress(ValueError):
                coord = normalize_coordinate(coord)

        self.available_coordinates.remove(coord)
        return coord


class ComputerPlayer(Player):
    def fire(self):
        coord = random.choice(tuple(self.available_coordinates))
        self.available_coordinates.remove(coord)
        return coord

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
