from .ship_board import ShipBoard
from .target_board import TargetBoard


class Player:
    def __init__(self, name: str = None):
        self.name = name
        self.ship_board = ShipBoard()
        self.target_board = TargetBoard()

    def move(self):
        raise NotImplementedError()

    def add(self):
        raise NotImplementedError()


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


class ComputerPlayer(Player):
    def move(self):
        pass

    def add(self):
        return [input("Enter ship coordinates: ").split() for _ in range(5)]
