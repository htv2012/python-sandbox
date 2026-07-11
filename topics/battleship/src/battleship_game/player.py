import random

from .const import COLS, ROWS
from .logger import logger
from .ship_board import ShipBoard
from .target_board import TargetBoard


class Player:
    def __init__(self, name: str = None):
        self.name = name
        self.ship_board = ShipBoard()
        self.target_board = TargetBoard()

    @property
    def is_lost(self) -> bool:
        return self.ship_board.all_sunk

    def assess(self, coord):
        return self.ship_board.assess(coord)

    def move(self):
        raise NotImplementedError()

    def add(self):
        raise NotImplementedError()

    def mark(self, coord, result):
        """Mark the target board."""
        raise NotImplementedError("mark")


class HumanPlayer(Player):
    def add_ships(self):
        self.ship_board.add("A1", "A2", "A3")
        self.ship_board.add("B1", "B2", "B3")
        self.ship_board.add("C1", "C2", "C3", "C4")
        self.ship_board.add("D1", "D2", "D3", "D4", "D5")
        self.ship_board.add("E1", "E2")

    def move(self):
        pass

    def add(self):
        for _ in range(5):
            coordinates = input("Enter ship coordinates: ").upper().split()
            self.ship_board.add(*coordinates)

    def mark(self, coord, result):
        """Mark the target board."""
        self.target_board.mark(coord, result)


class ComputerPlayer(Player):
    def move(self):
        pass

    def add(self):
        pass

    def add_ships(self):
        occupied = set()
        for ship_id, ship_size in enumerate([3, 3, 4, 5, 2]):
            conflicted = True
            while conflicted:
                direction = random.choice(["vertical", "horizontal"])
                if direction == "vertical":
                    row_index = random.randint(0, len(ROWS) - ship_size)
                    col_index = random.randint(0, len(COLS) - 1)
                    ship = [
                        ROWS[row_index + i] + COLS[col_index] for i in range(ship_size)
                    ]
                else:
                    row_index = random.randint(0, len(ROWS) - 1)
                    col_index = random.randint(0, len(COLS) - ship_size)
                    ship = [
                        ROWS[row_index] + COLS[col_index + i] for i in range(ship_size)
                    ]
                conflicted = any(coord in occupied for coord in ship)
                logger.debug("occupied: %r", occupied)
                logger.debug(
                    "ship ID: %d, ship: %r, conflicted: %r", ship_id, ship, conflicted
                )

            self.ship_board.add(*ship)
