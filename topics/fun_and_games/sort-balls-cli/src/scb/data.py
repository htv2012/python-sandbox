import io

STACK_CAPCACITY = 8


class Stack:
    def __init__(self):
        self._data = []

    def __repr__(self):
        return repr(self._data)

    @property
    def is_empty(self) -> bool:
        return len(self._data) == 0

    @property
    def is_full(self) -> bool:
        return len(self._data) == STACK_CAPCACITY

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
        while len(out) < STACK_CAPCACITY:
            out.append(" ")
        out.reverse()
        return iter(out)

    @property
    def is_completed(self) -> bool:
        return not self.is_empty and all(v == self._data[0] for v in self)


class Grid:
    def __init__(self):
        self._stacks = [Stack() for _ in range(8)]

    def __iter__(self):
        return iter(self._stacks)

    def __repr__(self):
        buf = io.StringIO()
        buf.write("\n")
        buf.write("| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |\n")
        buf.write("|---|---|---|---|---|---|---|---|\n")
        for row in zip(*[list(stack) for stack in self]):
            buf.write("| ")
            buf.write(" | ".join(row))
            buf.write(" |\n")

        buf.write("  ")
        buf.write("   ".join("!" if stack.is_completed else " " for stack in self))
        buf.write("  \n")
        return buf.getvalue()

    def put(self, stack_number: int, value):
        self._stacks[stack_number].push(value)

    def move(self, from_stack: int, to_stack: int):
        value = self._stacks[from_stack].pop()
        try:
            self._stacks[to_stack].push(value)
        except ValueError:
            self._stacks[from_stack].push(value)
            raise ValueError("Cannot move to a full stack")

    @property
    def completed(self) -> bool:
        return sum(1 if stack.is_completed else 0 for stack in self) == 7
