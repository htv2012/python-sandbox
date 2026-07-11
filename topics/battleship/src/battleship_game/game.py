import contextlib

from .const import ALL_COORDINATES, normalize_coordinate
from .player import ComputerPlayer, HumanPlayer


class Game:
    def __init__(self):
        self.human = HumanPlayer()
        self.computer = ComputerPlayer()

    def start(self):
        self.human.add_ships()
        self.computer.add_ships()

    def human_fire(self):
        coord = None
        while coord not in ALL_COORDINATES:
            coord = input("Coordinate: ").upper()
            with contextlib.suppress(ValueError):
                coord = normalize_coordinate(coord)

        result = self.computer.assess(coord)
        print(f"{coord} -> {result}")
        self.human.mark(coord, result)

    @property
    def game_over(self) -> bool:
        """When one of the player wins."""
        return self.human.is_lost or self.computer.is_lost

    def print(self):
        """Show human ship- and target boards."""
        sb = str(self.human.ship_board).splitlines()
        tb = str(self.human.target_board).splitlines()
        sep = " " * 8
        for line in zip(sb, tb):
            print(sep.join(line))
