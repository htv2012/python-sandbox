# sandbox.py
import curses
import enum
import io
import random

from .grid import Grid
from .stack import CAPACITY, EMPTY_VALUE

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)


class Choice(enum.Enum):
    MOVE = enum.auto()
    QUIT = enum.auto()
    REPEAT = enum.auto()
    FILL = enum.auto()


class Asset(enum.StrEnum):
    EMPTY = "◼️"


class UserInput:
    pass


def draw_grid(screen: curses.window, grid: Grid):

    screen.clear()
    screen.addstr(1, 1, "SORT COLOR BALLS")

    y = 5
    x = 1
    empty_row = "│ " + " │ ".join([Asset.EMPTY] * 8) + " │"
    screen.addstr(y, x, empty_row)
    screen.addstr(y + 1, x, "│ 0️⃣ │ 1️⃣ │ 2️⃣ │ 3️⃣ │ 4️⃣ │ 5️⃣ │ 6️⃣ │ 7️⃣ │")

    for dy, row in enumerate(zip(*[stack.as_column for stack in grid]), 2):
        buf = io.StringIO()
        buf.write("│ ")
        buf.write(" │ ".join("◼️" if c == EMPTY_VALUE else c for c in row))
        buf.write(" │")
        screen.addstr(y + dy, x, buf.getvalue())

    screen.refresh()


def create_grid() -> Grid:
    grid = Grid()

    balls = "".join(ch * 8 for ch in "🔴🟠🟡🟢🔵🟣🟤")
    balls = list(balls)
    random.shuffle(balls)
    for i, ball in enumerate(balls):
        stack_number = i // CAPACITY
        grid.put(stack_number, ball)

    return grid


def _main(screen: curses.window):
    curses.curs_set(0)

    grid = create_grid()
    user_input = UserInput()
    while True:
        draw_grid(screen, grid)
        break
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
            draw_grid(grid)
            print("Sorted!")
            break

    screen.getkey()


def main():
    curses.wrapper(_main)
