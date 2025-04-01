#!/usr/bin/env python3
import collections


class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    @classmethod
    def from_iterable(cls, iterable):
        nodes = iter(iterable)
        root = Tree(next(nodes))
        for data in nodes:
            root.insert(data)

        return root

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Tree(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Tree(data)
            else:
                self.right.insert(data)

    def preorder(self, visit_function):
        visit_function(self.data)
        if self.left:
            self.left.preorder(visit_function)
        if self.right:
            self.right.preorder(visit_function)

    def postorder(self, visit_function):
        if self.left:
            self.left.preorder(visit_function)
        if self.right:
            self.right.preorder(visit_function)
        visit_function(self.data)

    def __repr__(self):
        return "[{}]".format(self.data)

    def print(self, handle=None, level=0):
        if self.right is not None:
            self.right.print(level=level + 1)
        print(f"{' ' * 4 * level}->({self.data})")
        if self.left is not None:
            self.left.print(level=level + 1)


def _update_queue_and_grid(node, queue, grid, column_number):
    if node is None:
        return
    grid[column_number].append(node.data)
    if node.left or node.right:
        queue.append((node, column_number))


def vertical(root):
    """
    Performs a vertical traversal
    """
    if root is None:
        return {}

    queue = collections.deque()

    grid = collections.defaultdict(list)
    _update_queue_and_grid(root, queue, grid, 0)

    while queue:
        node, column_number = queue.popleft()
        _update_queue_and_grid(node.left, queue, grid, column_number - 1)
        _update_queue_and_grid(node.right, queue, grid, column_number + 1)

    return grid


def _column_view(root, row_index):
    grid = vertical(root)
    for _, column in sorted(grid.items()):
        yield column[row_index]


def top_view(root):
    return _column_view(root, row_index=0)


def bottom_view(root):
    return _column_view(root, row_index=-1)
