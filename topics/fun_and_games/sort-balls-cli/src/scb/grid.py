from .stack import Stack

COLUMNS_COUNT = 8

ball_table = {
    "a": "🔴",
    "b": "🟠",
    "c": "🟡",
    "d": "🟢",
    "e": "🔵",
    "f": "🟣",
    "g": "🟤",
    " ": "◼️",
}


class Grid:
    def __init__(self):
        self._stacks = [Stack() for _ in range(COLUMNS_COUNT)]

    def __iter__(self):
        return iter(self._stacks)

    def __getitem__(self, key) -> Stack:
        return self._stacks[key]

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
