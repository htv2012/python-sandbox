# sandbox.py
import collections
import curses
import enum
import io
import random

from .grid import COLUMNS_COUNT, Grid
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


class State(enum.Enum):
    POP = enum.auto()
    PUSH = enum.auto()
    NONE = enum.auto()


class Asset(enum.StrEnum):
    EMPTY = "◼️"
    POP = "⬆"
    PUSH = "⬇"
    # ⬆ ⬇ ↑ ↓
    BALL1 = "🔴"
    BALL2 = "🟠"
    BALL3 = "🟡"
    BALL4 = "🟢"
    BALL5 = "🔵"
    BALL6 = "🟣"
    BALL7 = "🟤"

    @classmethod
    def balls(cls):
        return [
            Asset.BALL1,
            Asset.BALL2,
            Asset.BALL3,
            Asset.BALL4,
            Asset.BALL5,
            Asset.BALL6,
            Asset.BALL7,
        ]


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


def diag() -> Grid:
    grid = Grid()
    balls = collections.deque(Asset.balls())
    for i in range(CAPACITY):
        for stack, ball in zip(grid[:-1], balls):
            stack.push(ball)
        balls.rotate(1)

    return grid


def create_grid() -> Grid:
    grid = Grid()

    balls = "".join(ch * 8 for ch in "🔴🟠🟡🟢🔵🟣🟤")
    balls = list(balls)
    random.shuffle(balls)
    for i, ball in enumerate(balls):
        stack_number = i // CAPACITY
        grid.put(stack_number, ball)

    return grid


def get_user_input(stdscr: curses.window, col: int, state: State):
    y = 15
    x = 3
    stdscr.addstr(y, x, Asset.POP if state == State.POP else Asset.PUSH)
    while True:
        key = stdscr.getch()
        if key == curses.KEY_RIGHT:
            stdscr.addstr(y, x, " ")
            col = (col + 1) % COLUMNS_COUNT
            x = 3 + (col * 5)
            stdscr.addstr(y, x, Asset.POP if state == State.POP else Asset.PUSH)
        elif key == curses.KEY_LEFT:
            stdscr.addstr(y, x, " ")
            col = (col - 1) % COLUMNS_COUNT
            x = 3 + (col * 5)
            stdscr.addstr(y, x, Asset.POP if state == State.POP else Asset.PUSH)
        elif key == ord(" "):
            return col
        elif key == ord("q"):
            break


def _main(stdscr: curses.window):
    curses.curs_set(0)
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(True)

    # grid = create_grid()
    grid = diag()
    col = 0
    state = State.POP

    while True:
        draw_grid(stdscr, grid)
        get_user_input(stdscr, col, state)
        break
        # if choice == Choice.QUIT:
        #     break
        # elif choice == Choice.MOVE:
        #     src, dest = args
        #     try:
        #         grid.move(from_stack=src, to_stack=dest)
        #     except ValueError as err:
        #         print(err)
        # elif choice == Choice.FILL:
        #     picked, dest = args
        #     for src, stack in enumerate(grid):
        #         if src == dest:
        #             continue
        #         while stack.top == picked:
        #             if grid[dest].is_full:
        #                 break
        #             stack.pop()
        #             grid[dest].push(picked)

        # if grid.completed:
        #     draw_grid(grid)
        #     print("Sorted!")
        #     break

    # stdscr.getkey()


def main():
    curses.wrapper(_main)
