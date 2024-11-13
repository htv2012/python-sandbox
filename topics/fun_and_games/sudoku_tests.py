"""
Test Sudoku routines
"""
import unittest

import sudoku4 as su


class SudokuTests(unittest.TestCase):
    def test_nw_corner(self):
        self.assertEqual(('A', 0), su.nw_corner(('A', 0)))
        self.assertEqual(('A', 0), su.nw_corner(('A', 1)))
        self.assertEqual(('A', 0), su.nw_corner(('A', 2)))
        self.assertEqual(('A', 0), su.nw_corner(('B', 0)))
        self.assertEqual(('A', 0), su.nw_corner(('B', 1)))
        self.assertEqual(('A', 0), su.nw_corner(('B', 2)))
        self.assertEqual(('A', 0), su.nw_corner(('C', 0)))
        self.assertEqual(('A', 0), su.nw_corner(('C', 1)))
        self.assertEqual(('A', 0), su.nw_corner(('C', 2)))

        self.assertEqual(('A', 3), su.nw_corner(('A', 3)))
        self.assertEqual(('A', 3), su.nw_corner(('A', 4)))
        self.assertEqual(('A', 3), su.nw_corner(('A', 5)))
        self.assertEqual(('A', 3), su.nw_corner(('B', 3)))
        self.assertEqual(('A', 3), su.nw_corner(('B', 4)))
        self.assertEqual(('A', 3), su.nw_corner(('B', 5)))
        self.assertEqual(('A', 3), su.nw_corner(('C', 3)))
        self.assertEqual(('A', 3), su.nw_corner(('C', 4)))
        self.assertEqual(('A', 3), su.nw_corner(('C', 5)))

        self.assertEqual(('A', 6), su.nw_corner(('A', 6)))
        self.assertEqual(('A', 6), su.nw_corner(('A', 7)))
        self.assertEqual(('A', 6), su.nw_corner(('A', 8)))
        self.assertEqual(('A', 6), su.nw_corner(('B', 6)))
        self.assertEqual(('A', 6), su.nw_corner(('B', 7)))
        self.assertEqual(('A', 6), su.nw_corner(('B', 8)))
        self.assertEqual(('A', 6), su.nw_corner(('C', 6)))
        self.assertEqual(('A', 6), su.nw_corner(('C', 7)))
        self.assertEqual(('A', 6), su.nw_corner(('C', 8)))

        self.assertEqual(('D', 0), su.nw_corner(('D', 0)))
        self.assertEqual(('D', 0), su.nw_corner(('D', 1)))
        self.assertEqual(('D', 0), su.nw_corner(('D', 2)))
        self.assertEqual(('D', 0), su.nw_corner(('E', 0)))
        self.assertEqual(('D', 0), su.nw_corner(('E', 1)))
        self.assertEqual(('D', 0), su.nw_corner(('E', 2)))
        self.assertEqual(('D', 0), su.nw_corner(('F', 0)))
        self.assertEqual(('D', 0), su.nw_corner(('F', 1)))
        self.assertEqual(('D', 0), su.nw_corner(('F', 2)))

        self.assertEqual(('D', 3), su.nw_corner(('D', 3)))
        self.assertEqual(('D', 3), su.nw_corner(('D', 4)))
        self.assertEqual(('D', 3), su.nw_corner(('D', 5)))
        self.assertEqual(('D', 3), su.nw_corner(('E', 3)))
        self.assertEqual(('D', 3), su.nw_corner(('E', 4)))
        self.assertEqual(('D', 3), su.nw_corner(('E', 5)))
        self.assertEqual(('D', 3), su.nw_corner(('F', 3)))
        self.assertEqual(('D', 3), su.nw_corner(('F', 4)))
        self.assertEqual(('D', 3), su.nw_corner(('F', 5)))

        self.assertEqual(('D', 6), su.nw_corner(('D', 6)))
        self.assertEqual(('D', 6), su.nw_corner(('D', 7)))
        self.assertEqual(('D', 6), su.nw_corner(('D', 8)))
        self.assertEqual(('D', 6), su.nw_corner(('E', 6)))
        self.assertEqual(('D', 6), su.nw_corner(('E', 7)))
        self.assertEqual(('D', 6), su.nw_corner(('E', 8)))
        self.assertEqual(('D', 6), su.nw_corner(('F', 6)))
        self.assertEqual(('D', 6), su.nw_corner(('F', 7)))
        self.assertEqual(('D', 6), su.nw_corner(('F', 8)))

        self.assertEqual(('G', 0), su.nw_corner(('G', 0)))
        self.assertEqual(('G', 0), su.nw_corner(('G', 1)))
        self.assertEqual(('G', 0), su.nw_corner(('G', 2)))
        self.assertEqual(('G', 0), su.nw_corner(('H', 0)))
        self.assertEqual(('G', 0), su.nw_corner(('H', 1)))
        self.assertEqual(('G', 0), su.nw_corner(('H', 2)))
        self.assertEqual(('G', 0), su.nw_corner(('I', 0)))
        self.assertEqual(('G', 0), su.nw_corner(('I', 1)))
        self.assertEqual(('G', 0), su.nw_corner(('I', 2)))

        self.assertEqual(('G', 3), su.nw_corner(('G', 3)))
        self.assertEqual(('G', 3), su.nw_corner(('G', 4)))
        self.assertEqual(('G', 3), su.nw_corner(('G', 5)))
        self.assertEqual(('G', 3), su.nw_corner(('H', 3)))
        self.assertEqual(('G', 3), su.nw_corner(('H', 4)))
        self.assertEqual(('G', 3), su.nw_corner(('H', 5)))
        self.assertEqual(('G', 3), su.nw_corner(('I', 3)))
        self.assertEqual(('G', 3), su.nw_corner(('I', 4)))
        self.assertEqual(('G', 3), su.nw_corner(('I', 5)))

        self.assertEqual(('G', 6), su.nw_corner(('G', 6)))
        self.assertEqual(('G', 6), su.nw_corner(('G', 7)))
        self.assertEqual(('G', 6), su.nw_corner(('G', 8)))
        self.assertEqual(('G', 6), su.nw_corner(('H', 6)))
        self.assertEqual(('G', 6), su.nw_corner(('H', 7)))
        self.assertEqual(('G', 6), su.nw_corner(('H', 8)))
        self.assertEqual(('G', 6), su.nw_corner(('I', 6)))
        self.assertEqual(('G', 6), su.nw_corner(('I', 7)))
        self.assertEqual(('G', 6), su.nw_corner(('I', 8)))

    def test_same_box(self):
        self.assertTrue(su.same_box(('A', 0), ('A', 0)))
        self.assertTrue(su.same_box(('A', 0), ('A', 1)))
        self.assertTrue(su.same_box(('A', 0), ('A', 2)))
        self.assertTrue(su.same_box(('A', 0), ('B', 0)))
        self.assertTrue(su.same_box(('A', 0), ('B', 1)))
        self.assertTrue(su.same_box(('A', 0), ('B', 2)))
        self.assertTrue(su.same_box(('A', 0), ('C', 0)))
        self.assertTrue(su.same_box(('A', 0), ('C', 1)))
        self.assertTrue(su.same_box(('A', 0), ('C', 2)))

        self.assertTrue(su.same_box(('G', 0), ('G', 0)))
        self.assertTrue(su.same_box(('G', 0), ('G', 1)))
        self.assertTrue(su.same_box(('G', 0), ('G', 2)))
        self.assertTrue(su.same_box(('G', 0), ('H', 0)))
        self.assertTrue(su.same_box(('G', 0), ('H', 1)))
        self.assertTrue(su.same_box(('G', 0), ('H', 2)))
        self.assertTrue(su.same_box(('G', 0), ('I', 0)))
        self.assertTrue(su.same_box(('G', 0), ('I', 1)))
        self.assertTrue(su.same_box(('G', 0), ('I', 2)))


if __name__ == '__main__':
    unittest.main()
