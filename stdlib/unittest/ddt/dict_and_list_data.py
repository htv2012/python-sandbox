# encoding: utf-8

import unittest
import ddt


input_data = {
    'bone': ['bone.txt', 5],
    'knee': ['knee.txt', 6]}
idata2 = [
    ['bone.txt', 5],
    ['knee.txt', 6]]


@ddt.ddt
class FooTest(unittest.TestCase):
    @ddt.data(*input_data)
    def test_body(self, key):
        filename, threshold = input_data[key]
        self.assertLess(threshold, 10)
        self.assertTrue(filename.endswith('.txt'))

    @ddt.data(*idata2)
    def test_body2(self, test_data_list):
        filename, threshold = test_data_list
        self.assertLess(threshold, 10)
        self.assertTrue(filename.endswith('.txt'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
