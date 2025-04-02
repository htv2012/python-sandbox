import io

from .ship_board import ShipBoard
from .target_board import TargetBoard


class GameBoard:
    def __init__(self):
        self.ship = ShipBoard()
        self.target = TargetBoard()

    def __str__(self):
        buf = io.StringIO()
        ship_text = str(self.ship).splitlines()
        target_text = str(self.target).splitlines()
        for line in zip(ship_text, target_text):
            buf.write("    ".join(line))
            buf.write("\n")

        return buf.getvalue()
