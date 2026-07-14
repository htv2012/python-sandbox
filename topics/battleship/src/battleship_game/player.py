import random

from . import const
from .log import logger
from .ship_board import ShipBoard
from .target_board import TargetBoard


class Player:
    def __init__(self):
        self.ship_board = ShipBoard()
        self.target_board = TargetBoard()
        self.available_coordinates = set(const.ALL_COORDINATES)

    def generate_ship(self, ship_size) -> list[str]:
        raise NotImplementedError("generate_ship")

    def load(self, filename):
        with open(filename) as stream:
            for ship_id, ship in zip(const.SHIP_IDS, stream):
                ship = [const.normalize_coordinate(c) for c in ship.split()]
                self.ship_board.add(ship_id, ship)

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

    def report(self, coord):
        return self.ship_board.report(coord)

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
    def __init__(self):
        super().__init__()
        self.candidates = []

    def find_target(self):
        while self.candidates:
            target = self.candidates.pop()
            if target in self.available_coordinates:
                logger.debug("target picked: %r", target)
                logger.debug("remaining candidates: %r", self.candidates)
                return target

        target = random.choice(tuple(self.available_coordinates))
        logger.debug("target picked randomly: %r", target)
        return target

    def add_candidates(self, coord):
        row, col = [ord(x) for x in coord]
        coords = []
        for i in range(1, 3):
            coords.append(chr(row - i) + chr(col))
            coords.append(chr(row + i) + chr(col))
            coords.append(chr(row) + chr(col - i))
            coords.append(chr(row) + chr(col + i))
        coords = [c for c in coords if c in self.available_coordinates]
        logger.debug("Hit %r, will try: %r", coord, coords)
        logger.debug("Candidates: %r", self.candidates)
        self.candidates.extend(coords)

    def mark(self, coord, result):
        """Mark the target board."""
        self.target_board.mark(coord, result)
        if result == const.MARK_HIT:
            self.add_candidates(coord)

    def fire(self):
        coord = self.find_target()
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
