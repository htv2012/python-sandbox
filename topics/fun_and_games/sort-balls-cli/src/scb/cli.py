import random

from .data import STACK_CAPCACITY, Grid


def get_input():
    while True:
        try:
            move = input("> ")
            if move == "q":
                return -1, -1
            src, dest = [int(v) for v in move]
            return src, dest
        except ValueError:
            pass


def main():
    grid = Grid()

    balls = "".join(ch * 8 for ch in "abcdefg")
    balls = list(balls)
    random.shuffle(balls)
    for i, ball in enumerate(balls):
        stack_number = i // STACK_CAPCACITY
        grid.put(stack_number, ball)

    while True:
        print(grid)
        src, dest = get_input()
        if src == -1:
            break

        try:
            grid.move(from_stack=src, to_stack=dest)
        except ValueError as err:
            print(err)

        if grid.completed:
            print("Completed!")
            break
