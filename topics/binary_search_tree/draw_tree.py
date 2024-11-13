#!/usr/bin/env python3
"""
Draws a binary search tree and save to a file
"""
import argparse
import collections

import pygraphviz

import tree


def get_edges(root):
    queue = collections.deque([root])
    while queue:
        node = queue.pop()
        if node.left is not None:
            yield node.data, node.left.data
            queue.append(node.left)
        if node.right is not None:
            yield node.data, node.right.data
            queue.append(node.right)

def main():
    """ Entry """
    parser = argparse.ArgumentParser()
    parser.add_argument("nodes", nargs="+", type=int)
    parser.add_argument("-o", "--output", default="out.png")
    options = parser.parse_args()

    root = tree.BinarySearchTree.from_sequence(options.nodes)
    graph = pygraphviz.AGraph(directed=True)
    graph.add_edges_from(get_edges(root))
    graph.draw(options.output, prog="dot")


if __name__ == "__main__":
    main()

