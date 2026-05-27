import enum
import random

from .grid import Grid
from .stack import CAPACITY


class Choice(enum.Enum):
    MOVE = enum.auto()
    QUIT = enum.auto()
    REPEAT = enum.auto()
    FILL = enum.auto()


class UserInput:
    def __init__(self):
        self.last = None

    def get(self) -> tuple[Choice, tuple]:
        while True:
            try:
                choice = input("> ")
                if choice == "" and self.last:
                    return self.last
                elif choice == "q":
                    return Choice.QUIT, tuple()
                elif len(choice) == 2 and choice.isnumeric():
                    self.last = Choice.MOVE, tuple(int(v) for v in choice)
                    return self.last
                elif len(choice) == 2 and choice[0] in "ropgybw":
                    dest = int(choice[1])
                    return Choice.FILL, (choice[0], dest)
            except ValueError:
                pass


def main():
    grid = Grid()
    user_input = UserInput()

    balls = "".join(ch * 8 for ch in "🔴🟠🟡🟢🔵🟣🟤")
    balls = list(balls)
    random.shuffle(balls)
    for i, ball in enumerate(balls):
        stack_number = i // CAPACITY
        grid.put(stack_number, ball)

    while True:
        print(grid)
        choice, args = user_input.get()
        if choice == Choice.QUIT:
            break
        elif choice == Choice.MOVE:
            src, dest = args
            try:
                grid.move(from_stack=src, to_stack=dest)
            except ValueError as err:
                print(err)
        elif choice == Choice.FILL:
            picked, dest = args
            for src, stack in enumerate(grid):
                if src == dest:
                    continue
                while stack.top == picked:
                    if grid[dest].is_full:
                        break
                    stack.pop()
                    grid[dest].push(picked)

        if grid.completed:
            print(grid)
            print("Sorted!")
            break
