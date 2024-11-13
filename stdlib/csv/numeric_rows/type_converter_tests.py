#!/usr/bin/env python
"""
Tests for the type_converter module
"""
import unittest
from type_converter import (
    from_hex_str,
    from_oct_str,
    from_bin_str,
)

class HexConverterTest(unittest.TestCase):
    def perform(self, expected, input_data):
        actual = from_hex_str(input_data)
        error_message = 'input: {}, expected: {}, actual: {}'.format(
            input_data, expected, actual)

        self.assertEqual(expected, actual, error_message)

    def test_happy_path_0X10(self):
        self.perform(expected=16, input_data='0X10')

    def test_happy_path_0x10(self):
        self.perform(expected=16, input_data='0x10')

    def test_happy_path_10(self):
        self.perform(expected=16, input_data='10')


if __name__ == '__main__':
    unittest.main()
