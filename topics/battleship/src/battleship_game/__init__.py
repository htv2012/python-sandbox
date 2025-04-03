from .game_board import GameBoard
from .player import Player
from .ship_board import ShipBoard
from .target_board import TargetBoard

__all__ = [
    "GameBoard",
    "ShipBoard",
    "TargetBoard",
    "Player",
]


def main() -> None:
    print("Hello from battleship-game!")
