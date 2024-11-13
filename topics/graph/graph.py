"""A homemade graph."""

import collections


class Graph:
    """An undirected graph."""

    def __init__(self, nodes=None, edges=None):
        self._node = collections.defaultdict(set)
        for node1, node2 in edges or []:
            self._node[node1].add(node2)
            self._node[node2].add(node1)

    @property
    def nodes(self):
        return list(self._node)

    def edges(self):
        seen = set()
        for node1, neighbors in self._node.items():
            for node2 in neighbors:
                edge = tuple(sorted([node1, node2]))
                if edge not in seen:
                    yield edge
                seen.add(edge)


def main():
    """Entry"""
    g = Graph(edges=[(0, 1), (0, 2), (1, 2)])
    print(f"Nodes: {g.nodes}")
    print("Edges:", end=" ")
    print(", ".join(repr(e) for e in g.edges()))


if __name__ == "__main__":
    main()
