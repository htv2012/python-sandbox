from typing import Iterator

from .stack import Stack

COLUMNS_COUNT = 8


class Grid:
    def __init__(self):
        self._stacks = [Stack() for _ in range(COLUMNS_COUNT)]

    def __iter__(self) -> Iterator[Stack]:
        return iter(self._stacks)

    def __getitem__(self, key) -> Stack:
        return self._stacks[key]

    def put(self, stack_number: int, value):
        self._stacks[stack_number].push(value)

    @property
    def top_balls(self) -> list:
        return [stack.top for stack in self]

    @property
    def completed(self) -> bool:
        return (
            sum(1 if stack.is_completed else 0 for stack in self) == COLUMNS_COUNT - 1
        )
