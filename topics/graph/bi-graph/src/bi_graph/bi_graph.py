import collections


def normalize_edge(node1, node2):
    if node1 < node2:
        return node1, node2
    else:
        return node2, node1


class BiGraph:
    def __init__(self):
        self.graph = collections.defaultdict(set)
        self.edges = set()
        self.nodes = set()

    def add_edge(self, node1, node2):
        edge = normalize_edge(node1, node2)
        if edge in self.edges:
            return

        self.edges.add(edge)
        self.nodes.add(node1)
        self.nodes.add(node2)

        self.graph[node1].add(node2)
        self.graph[node2].add(node1)

    def all_paths(self, source, dest):
        pass

