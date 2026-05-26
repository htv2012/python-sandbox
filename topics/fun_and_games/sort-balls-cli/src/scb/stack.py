CAPACITY = 8


class Stack:
    def __init__(self):
        self._data = []

    def __repr__(self):
        return f"Stack{self._data!r}"

    @property
    def is_empty(self) -> bool:
        return len(self._data) == 0

    @property
    def is_full(self) -> bool:
        return len(self._data) == CAPACITY

    @property
    def top(self):
        if self.is_empty:
            return " "
        return self._data[-1]

    def push(self, value):
        if self.is_full:
            raise ValueError("Push a full stack")
        self._data.append(value)

    def pop(self):
        if self.is_empty:
            raise ValueError("Pop an empty stack")
        return self._data.pop()

    def __iter__(self):
        out = self._data.copy()
        while len(out) < CAPACITY:
            out.append(" ")
        out.reverse()
        return iter(out)

    @property
    def is_completed(self) -> bool:
        return not self.is_empty and all(v == self._data[0] for v in self)
