#!/usr/bin/env python
"""
    A   B   C
  |---|---|---|
1 | x | o | o |
  |---|---|---|
2 | o | o | x |
  |---|---|---|
3 | x | x | o |
  |---|---|---|
"""

from __future__ import print_function, unicode_literals

import itertools
import logging
import os
from io import StringIO

try:
    input = raw_input  # Python 2
except NameError:
    pass  # Python 3


logging.basicConfig(level=os.getenv("LOGLEVEL", logging.DEBUG))
logger = logging.getLogger(__name__)


class Board(object):
    ALL_COORDINATES = ("A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3")
    EMPTY = " "
    X = "X"
    O = "O"

    def __init__(self):
        self.grid = dict.fromkeys(Board.ALL_COORDINATES, Board.EMPTY)
        self.VALID_COORDINATES = set(Board.ALL_COORDINATES)

    def __getitem__(self, key):
        return self.grid[key]

    def __setitem__(self, key, value):
        self.grid[key] = value

    def mark(self, coordinate, piece):
        self[coordinate] = piece
        self.VALID_COORDINATES.discard(piece)

    def __str__(self):
        buf = StringIO()
        buf.write("\n")
        buf.write("    A   B   C\n")
        buf.write("  |---|---|---|\n")
        buf.write(
            "1 | {} | {} | {} |\n".format(
                self.grid["A1"], self.grid["B1"], self.grid["C1"]
            )
        )
        buf.write("  |---|---|---|\n")
        buf.write(
            "2 | {} | {} | {} |\n".format(
                self.grid["A2"], self.grid["B2"], self.grid["C2"]
            )
        )
        buf.write("  |---|---|---|\n")
        buf.write(
            "3 | {} | {} | {} |\n".format(
                self.grid["A3"], self.grid["B3"], self.grid["C3"]
            )
        )
        buf.write("  |---|---|---|\n")
        return buf.getvalue()


class Player(object):
    class BadMove(Exception):
        pass

    def __init__(self, name, piece):
        self.name = name
        self.piece = piece
        self.prompt = ">>> {} ({}): ".format(self.name, self.piece)

    def ensure_valid_coordinate(self, coordinate, board):
        if coordinate not in board.VALID_COORDINATES:
            raise self.BadMove("Position is taken or out of range")

    def ensure_empty_square(self, coordinate, board):
        if board[coordinate] != board.EMPTY:
            raise self.BadMove("Cell is not empty: {}".format(coordinate))


class HumanPlayer(object):
    def make_a_move(self, board):
        while True:
            try:
                coordinate = input(self.prompt).upper()
                self.ensure_valid_coordinate(coordinate, board)
                self.ensure_empty_square(coordinate, board)
                return coordinate
            except self.BadMove as e:
                print(e)


class ComputerPlayer(Player):
    def make_a_move(self, board):
        # choice = random.choice(self.valid_coordinates
        pass


class Game(object):
    """A game controller"""

    def __init__(self, player1, player2, board):
        self.board = board
        self.turns = itertools.cycle((player1, player2))

    def start(self):
        message = "Tie"
        for _, player in zip(range(9), self.turns):
            print(self.board)

            coordinate = player.make_a_move(self.board)
            self.board.mark(coordinate, player.piece)

            if self.won(player.piece):
                message = "{} won".format(player.name)
                break

        print(self.board)
        print(message)

    def won(self, piece):
        winning_positions = [
            ("A1", "B1", "C1"),
            ("A2", "B2", "C2"),
            ("A3", "B3", "C3"),
            ("A1", "A2", "A3"),
            ("B1", "B2", "B3"),
            ("C1", "C2", "C3"),
            ("A1", "B2", "C3"),
            ("A3", "B2", "C1"),
        ]
        return any(
            all(self.board[coordinate] == piece for coordinate in coordinates)
            for coordinates in winning_positions
        )


def main():
    player_x_name = input("Player X name: ")
    player_o_name = input("Player O name: ")

    game = Game(
        HumanPlayer(player_x_name, Board.X),
        HumanPlayer(player_o_name, Board.O),
        Board(),
    )
    game.start()


if __name__ == "__main__":
    main()
