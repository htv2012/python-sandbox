import os
import unittest

import sudoku


EMPTY_BOARD = """. . . | . . . | . . .
. . . | . . . | . . .
. . . | . . . | . . .
------+-------+-------
. . . | . . . | . . .
. . . | . . . | . . .
. . . | . . . | . . .
------+-------+-------
. . . | . . . | . . .
. . . | . . . | . . .
. . . | . . . | . . .
""".strip() + ' \n'

script_dir = os.path.abspath(os.path.dirname(__file__))
board1_filename = os.path.join(script_dir, 'board1.txt')


class BoardTest(unittest.TestCase):
    def setUp(self):
        self.board = sudoku.Board()

    def test_can_create_empty(self):
        self.assertEqual(sudoku.EMPTY, self.board[0][0])

    def test_can_modify_cell(self):
        self.board[0][5] = '8'
        self.assertEqual('8', self.board[0][5])
        self.assertEqual(sudoku.EMPTY, self.board[1][5])

    def test_len(self):
        self.assertEqual(sudoku.ROWS, len(self.board))

    @unittest.skip('Need investigation')
    def test_print(self):
        as_string = str(self.board)
        self.assertEqual(EMPTY_BOARD, as_string)

    def test_read(self):
        with open(board1_filename) as f:
            self.board.read(f)

        self.assertEqual('5', self.board[0][0])
        self.assertEqual('6', self.board[4][4])
        self.assertEqual('1', self.board[8][8])


    def test_candidate_of_filled_cell(self):
        with open(board1_filename) as f:
            self.board.read(f)

            self.assertEqual([], self.board.candidates(0, 0))
            self.assertEqual([], self.board.candidates(4, 4))
            self.assertEqual([], self.board.candidates(8, 8))

if __name__ == '__main__':
    unittest.main()
