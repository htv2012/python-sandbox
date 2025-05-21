from .player import HumanPlayer, Player
from .ship_board import ShipBoard
from .target_board import TargetBoard

__all__ = [
    "HumanPlayer",
    "Player",
    "ShipBoard",
    "TargetBoard",
]


def main() -> None:
    print("Hello from battleship-game!")
