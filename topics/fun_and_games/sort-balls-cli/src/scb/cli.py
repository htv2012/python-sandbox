import collections
import random

from .grid import Grid
from .stack import CAPACITY


class UserInput:
    def __init__(self):
        self.last = None

    def get(self):
        while True:
            try:
                move = input("> ")
                if move == "" and self.last:
                    return self.last
                elif move == ".":
                    # TODO: crashed
                    self.last = (".", 9)
                    return self.last
                elif move == "q":
                    return -1, -1
                elif move.startswith("f"):
                    self.last = ("f", int(move[1]))
                    return self.last
                src, dest = [int(v) for v in move]
                self.last = src, dest
            except ValueError:
                pass


def main():
    grid = Grid()
    user_input = UserInput()

    balls = "".join(ch * 8 for ch in "abcdefg")
    balls = list(balls)
    random.shuffle(balls)
    for i, ball in enumerate(balls):
        stack_number = i // CAPACITY
        grid.put(stack_number, ball)

    while True:
        print(grid)
        src, dest = user_input.get()
        if src == -1:
            break
        elif src == "f":
            top = grid.top_balls
            counter = collections.Counter(top)
            # most_common() sample return: [('c', 3)]
            picked = counter.most_common(1)[0][0]
            for src, ball in enumerate(top):
                if grid[dest].is_full:
                    break
                if ball == picked:
                    grid.move(src, dest)
        else:
            try:
                grid.move(from_stack=src, to_stack=dest)
            except ValueError as err:
                print(err)

            if grid.completed:
                print(grid)
                print("Sorted!")
                break
