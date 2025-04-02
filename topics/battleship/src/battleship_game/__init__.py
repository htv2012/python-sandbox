from .game_board import GameBoard
from .ship_board import ShipBoard
from .target_board import TargetBoard

__all__ = [
    "GameBoard",
    "ShipBoard",
    "TargetBoard",
]


def main() -> None:
    print("Hello from battleship-game!")
