class Tree:
    def __init__(self, value, parent=None):
        self.value = value
        self._children = []
        self._parent = None
        self.parent = parent

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        self._parent = node
        if node is not None:
            node._children.append(self)

    def iter_children(self):
        return iter(self._children)

    def add_children(self, *children):
        for child in children:
            child.parent = self
