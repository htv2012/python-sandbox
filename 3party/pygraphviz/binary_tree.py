#!/usr/bin/env python3
"""
A simple binary tree
"""
import pygraphviz


def main():
    """ Entry """
    #       4
    #     /   \
    #    2      7
    #  /  \   /
    # 1    3 6
    graph = pygraphviz.AGraph(directed=True, landscape=False)
    graph.add_edge(4, 2)
    graph.add_edge(4, 7)
    graph.add_edge(2, 1)
    graph.add_edge(2, 3)
    graph.add_edge(7, 6)
    graph.draw("tree.png", prog="dot")


if __name__ == "__main__":
    main()

