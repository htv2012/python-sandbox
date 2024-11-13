"""
Test the Player class
"""
import unittest

from tictactoe import HumanPlayer


class MyBoard(object):
    valid_coordinates = ('A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3')
    EMPTY = ' '
    X = 'X'
    O = 'O'

    def __init__(self):
        self.grid = dict.fromkeys(self.valid_coordinates, self.EMPTY)

    def __getitem__(self, key):
        return self.grid[key]

    def __setitem__(self, key, value):
        self.grid[key] = value


class HumanPlayerTest(unittest.TestCase):
    def setUp(self):
        self.player1 = HumanPlayer('John', 'X')
        self.board = MyBoard()

    def test_create(self):
        self.assertEqual('John', self.player1.name)
        self.assertEqual('X', self.player1.piece)

    def test_ensure_valid_coordinate_expect_pass(self):
        for coordinate in self.board.valid_coordinates:
            self.player1.ensure_valid_coordinate(coordinate, self.board)

    def test_ensure_valid_coordinate_expect_fail(self):
        with self.assertRaises(HumanPlayer.BadMove):
            self.player1.ensure_valid_coordinate('A5', self.board)

    def test_ensure_empty_square_expect_no_exception(self):
        for coordinate in self.board.valid_coordinates:
            self.player1.ensure_empty_square(coordinate, self.board)

    def test_ensure_empty_square_expect_exception(self):
        coordinate = 'A3'
        self.board[coordinate] = self.board.X
        with self.assertRaises(HumanPlayer.BadMove):
            self.player1.ensure_empty_square(coordinate, self.board)


if __name__ == '__main__':
    unittest.main()
