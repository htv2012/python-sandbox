import collections
import logging

logger = logging.getLogger("bigraph")


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

    def valid_path(self, source, dest):
        logger.debug(f"{source = }, {dest = }")

        que = collections.deque()
        que.append(source)
        seen = set()

        while que:
            src = que.popleft()
            logger.debug(f"visit {src}")

            seen.add(src)
            for mid in self.graph[src]:
                logger.debug(f"  {mid = }")
                if mid in seen:
                    logger.debug(f"  {mid} has been visited, skip")
                    continue

                if mid == dest:
                    logger.debug(f"  path found {source} - {mid}")
                    return True

                logger.debug(f"  enqueue {mid}")
                que.append(mid)

            logger.debug(f"done {src}")

        return False
