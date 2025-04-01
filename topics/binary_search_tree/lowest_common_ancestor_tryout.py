#!/usr/bin/env python
# Find LCA

import unittest

from tree import BinarySearchTree


class LCATest(unittest.TestCase):
    def setUp(self):
        #      4
        #     /  \
        #    /    \
        #   2      6
        #  / \    / \
        # 1   3  5   7
        self.tree = BinarySearchTree.from_sequence("4261357")
        self.tree = BinarySearchTree.from_sequence((4, 2, 6, 1, 3, 5, 7))
        print("==== " + self.id())

    def test_lca_root1(self):
        self.assertEqual(self.tree, self.tree.lca(6, 2))

    def test_lca_root2(self):
        self.assertEqual(self.tree, self.tree.lca(2, 6))

    def test_lca_root_and_leaf(self):
        self.assertEqual(self.tree, self.tree.lca(4, 7))

    def test_search_left_tree1(self):
        self.assertEqual(self.tree.left, self.tree.lca(1, 3))

    def test_search_left_tree2(self):
        self.assertEqual(self.tree.left, self.tree.lca(3, 2))


if __name__ == "__main__":
    unittest.main()
