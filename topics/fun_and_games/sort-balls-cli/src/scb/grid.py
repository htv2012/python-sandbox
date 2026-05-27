import io

from .stack import Stack

COLUMNS_COUNT = 8


class Grid:
    def __init__(self):
        self._stacks = [Stack() for _ in range(COLUMNS_COUNT)]

    def __iter__(self):
        return iter(self._stacks)

    def __getitem__(self, key) -> Stack:
        return self._stacks[key]

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
        buf.write("   ".join("x" if stack.is_completed else " " for stack in self))
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
    def top_balls(self) -> list:
        return [stack.top for stack in self]

    @property
    def completed(self) -> bool:
        return sum(1 if stack.is_completed else 0 for stack in self) == 7
