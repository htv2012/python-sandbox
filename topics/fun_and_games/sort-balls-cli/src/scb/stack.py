CAPACITY = 8
EMPTY_VALUE = None


class Stack:
    def __init__(self):
        self.data = []

    def __repr__(self):
        return f"Stack{self.data!r}"

    def __iter__(self):
        return iter(self.data)

    @property
    def is_empty(self) -> bool:
        return len(self.data) == 0

    @property
    def is_full(self) -> bool:
        return len(self.data) == CAPACITY

    @property
    def top(self):
        if self.is_empty:
            return EMPTY_VALUE
        return self.data[-1]

    def push(self, value):
        if self.is_full:
            raise ValueError("Push a full stack")
        self.data.append(value)

    def pop(self):
        if self.is_empty:
            raise ValueError("Pop an empty stack")
        return self.data.pop()

    @property
    def as_column(self):
        out = self.data.copy()
        while len(out) < CAPACITY:
            out.append(EMPTY_VALUE)
        out.reverse()
        return out

    @property
    def is_completed(self) -> bool:
        return self.is_full and all(v == self.data[0] for v in self.as_column)
