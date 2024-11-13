#!/usr/bin/env python

import unittest

from maze import Cell, find_path
import yaml
import ddt
import os
import logging
from yaml2json import yaml2json


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


test_cases_filename_yaml = os.path.join(os.path.dirname(__file__), 'maze_test_cases.yaml')
# test_cases_filename_json = os.path.join(os.path.dirname(__file__), 'maze_test_cases.json')
test_cases_filename_json = yaml2json(test_cases_filename_yaml)
assert os.path.exists(test_cases_filename_json)



@ddt.ddt
class MazeTest(unittest.TestCase):
    @ddt.file_data(test_cases_filename_json)
    def test_paths(self, edges, expected_path, a, b):
        logger.info('Entering %s', self.id())
        logger.debug('Edges: %r', edges)
        logger.debug('Expected Path: %r', expected_path)
        cells = [Cell(name, neighbors) for name, neighbors in list(edges.items())]

    # def test_same_cell(self):
    #     start = Cell()
    #     expected = [start]
    #     self.assertEqual(expected, find_path(start, start))
    #
    # def test_not_same_cell(self):
    #     start = Cell()
    #     dest = Cell()
    #     self.assertNotEqual([start], find_path(start, dest))
    #     self.assertNotEqual([dest], find_path(start, dest))
    #
    # def test_one_step(self):
    #     start = Cell()
    #     dest = Cell()
    #     start.neighbors.append(dest)
    #     dest.neighbors.append(start)
    #     self.assertEqual([start, dest], find_path(start, dest))
    #
    # def test_two_steps(self):
    #     cells = [Cell(), Cell(), Cell()]
    #     cells[0].neighbors.append(cells[1])
    #     cells[1].neighbors.append(cells[0])
    #     cells[1].neighbors.append(cells[2])
    #     cells[2].neighbors.append(cells[1])
    #     self.assertEqual(cells, find_path(cells[0], cells[2]))
    #
    # def test_multiple_paths(self):
    #     start = Cell()
    #     mid = [Cell() for _ in range(3)]
    #     dest = Cell()
    #
    #     start.neighbors.append(mid[1])
    #     mid[1].neighbors.append(mid[0])
    #     mid[1].neighbors.append(mid[2])
    #     mid[1].neighbors.append(dest)
    #     # mid[2].neighbors.append(dest)
    #     self.assertEqual([start, mid[1], dest], find_path(start, dest))
    #
    # def test_circular(self):
    #     start = Cell()
    #     mid = [Cell() for _ in range(3)]
    #     dest = Cell()
    #
    #     start.neighbors.append(mid[1])
    #     mid[1].neighbors.append(mid[0])
    #     mid[1].neighbors.append(mid[2])
    #     mid[1].neighbors.append(dest)
    #     self.assertEqual([start, mid[1], dest], find_path(start, dest))


if __name__ == '__main__':
    unittest.main()
