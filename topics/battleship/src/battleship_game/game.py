import argparse

from . import const
from .player import ComputerPlayer, HumanPlayer


class Game:
    def __init__(self, filename):
        self.filename = filename
        self.human = HumanPlayer()
        self.computer = ComputerPlayer()

    def add_ships(self, filename):
        """Add ships on both sides.

        If filename is supplied, load the coordinates for human.
        """
        if filename is not None:
            self.human.load(filename)
        else:
            self.human.add_ships()
        self.computer.add_ships()
        self.print()

    def start(self):
        self.add_ships(self.filename)

        shooter, target = self.human, self.computer
        while not self.game_over:
            coord = shooter.fire()
            result = target.report(coord)
            shooter.mark(coord, result)

            self.print()
            shooter, target = target, shooter

        if self.human.is_lost:
            print("You lost")
        else:
            print("You won")

    @property
    def game_over(self) -> bool:
        """When one of the player wins."""
        return self.human.is_lost or self.computer.is_lost

    def print(self):
        """Show human ship- and target boards."""
        sb = str(self.human.ship_board).splitlines()
        tb = str(self.human.target_board).splitlines()
        sep = " " * const.BOARD_GAP
        for line in zip(sb, tb):
            print(sep.join(line))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file")
    args = parser.parse_args()

    game = Game(args.file)
    game.start()
