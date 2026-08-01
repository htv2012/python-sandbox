"""Monotonic Stack."""

import collections
import operator


class MonotonicStack:
    def __init__(self, increasing: bool = True):
        self.increasing = increasing
        self.stack = collections.deque()
        self.must_pop = operator.gt if increasing else operator.lt

    def push(self, value):
        while self.stack and self.must_pop(self.stack[-1], value):
            self.stack.pop()
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def __repr__(self):
        return (
            f"<MonotonicStack {'inc' if self.increasing else 'dec'} {list(self.stack)}>"
        )

    @property
    def empty(self):
        return len(self.stack) == 0
