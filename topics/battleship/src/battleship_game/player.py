import random

from . import const
from .ship_board import ShipBoard
from .target_board import TargetBoard


class Player:
    def __init__(self):
        self.ship_board = ShipBoard()
        self.target_board = TargetBoard()
        self.available_coordinates = set(const.ALL_COORDINATES)

    def generate_ship(self, ship_size) -> list[str]:
        raise NotImplementedError("generate_ship")

    def add_ships(self):
        occupied = set()
        for ship_id, ship_size in zip(const.SHIP_IDS, const.SHIP_SIZES):
            conflicted = True
            while conflicted:
                ship = self.generate_ship(ship_size)
                conflicted = any(c in occupied for c in ship)

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
    def generate_ship(self, ship_size) -> list[str]:
        print(self.ship_board)
        valid = False
        while not valid:
            ship = input(f"Ship (size={ship_size}): ").upper().split()
            ship = [const.normalize_coordinate(c) for c in ship]
            valid = (len(set(ship)) == ship_size) and all(
                c in const.ALL_COORDINATES for c in ship
            )
        return ship

    def fire(self):
        prompt = " " * (const.BOARD_WIDTH + const.BOARD_GAP) + "Coordinates: "
        coord = None
        while coord not in self.available_coordinates:
            coord = input(prompt).upper()
            coord = const.normalize_coordinate(coord)

        self.available_coordinates.remove(coord)
        return coord


class ComputerPlayer(Player):
    def fire(self):
        coord = random.choice(tuple(self.available_coordinates))
        self.available_coordinates.remove(coord)
        return coord

    def generate_ship(self, ship_size) -> list[str]:
        direction = random.choice(["vertical", "horizontal"])
        if direction == "vertical":
            row_index = random.randint(0, len(const.ROWS) - ship_size)
            col_index = random.randint(0, len(const.COLS) - 1)
            ship = [
                const.ROWS[row_index + i] + const.COLS[col_index]
                for i in range(ship_size)
            ]
        else:
            row_index = random.randint(0, len(const.ROWS) - 1)
            col_index = random.randint(0, len(const.COLS) - ship_size)
            ship = [
                const.ROWS[row_index] + const.COLS[col_index + i]
                for i in range(ship_size)
            ]
        return ship
