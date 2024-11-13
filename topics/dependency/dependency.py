import copy


class Dependency:
    def __init__(self):
        self._data = {}

    def add(self, name, dependencies):
        node = self._data.setdefault(name, set())
        for dependency in dependencies:
            node.add(dependency)
            self._data.setdefault(dependency, set())

    def resolve(self):
        nodes = copy.deepcopy(self._data)
        while nodes:
            names = list(nodes)
            ready = set()
            for name in names:
                if not nodes[name]:
                    # name does not have any dependencies
                    ready.add(name)
                    del nodes[name]
                    for value in nodes.values():
                        value.discard(name)
            yield ready

    def serial_resolve(self):
        for group in self.resolve():
            yield from group

    def nodes(self):
        return iter(self._data)
