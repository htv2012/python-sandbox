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


# TODO: Delete
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
    CHECKED = "✅"
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


class Coord:
    GRID_TOP_LEFT = (5, 1)
    MESSAGE = (20, 1)


# TODO: Use h, l, space for left, right, push/pop
class Action:
    LEFT = curses.KEY_LEFT
    RIGHT = curses.KEY_RIGHT
    POP = curses.KEY_UP
    PUSH = curses.KEY_DOWN
    QUIT = ord("q")


def draw_grid(stdscr: curses.window, grid: Grid, ball: str, col: int):

    stdscr.clear()
    stdscr.addstr(1, 1, "SORT COLOR BALLS")

    y, x = Coord.GRID_TOP_LEFT

    # Draw the "popped" ball
    stdscr.addstr(y - 1, 3 + (col * 5), ball)

    for dy, row in enumerate(zip(*[stack.as_column for stack in grid])):
        buf = io.StringIO()
        buf.write("│ ")
        buf.write(" │ ".join("◼️" if c == EMPTY_VALUE else c for c in row))
        buf.write(" │")
        stdscr.addstr(y + dy + 1, x, buf.getvalue())

    # Draw the solved indicators
    indicators = [
        Asset.CHECKED if stack.is_completed else Asset.EMPTY for stack in grid
    ]
    stdscr.addstr(y + 9, x, "├────┼────┼────┼────┼────┼────┼────┼────┤")
    stdscr.addstr(y + 10, x, "│ " + " │ ".join(indicators) + " │")

    stdscr.refresh()


def diag_grid() -> Grid:
    grid = Grid()
    balls = collections.deque(Asset.balls())
    for i in range(CAPACITY):
        for stack, ball in zip(grid[:-1], balls):
            stack.push(ball)
        balls.rotate(1)

    return grid


def random_grid() -> Grid:
    grid = Grid()

    balls = "".join(ch * 8 for ch in Asset.balls())
    balls = list(balls)
    random.shuffle(balls)
    for i, ball in enumerate(balls):
        stack_number = i // CAPACITY
        grid.put(stack_number, ball)

    return grid


def create_grid() -> Grid:
    return random.choice([diag_grid, random_grid])()


def get_user_input(stdscr: curses.window, column: int, cursor: str):
    y = 16
    x = 3 + (column * 5)
    stdscr.addstr(y, x, cursor)
    
    while True:
        key = stdscr.getch()
        if key == Action.RIGHT:
            stdscr.addstr(y, x, " ")
            column = (column + 1) % COLUMNS_COUNT
            x = 3 + (column * 5)
            stdscr.addstr(y, x, cursor)
        elif key == Action.LEFT:
            stdscr.addstr(y, x, " ")
            column = (column - 1) % COLUMNS_COUNT
            x = 3 + (column * 5)
            stdscr.addstr(y, x, cursor)
        elif key == Action.POP:
            return Action.POP, column
        elif key == Action.PUSH:
            return Action.PUSH, column
        elif key == Action.QUIT:
            return Action.QUIT, -1


def _main(stdscr: curses.window):
    curses.curs_set(0)
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(True)

    grid = create_grid()
    column = 0
    state = State.POP
    ball = " "

    while True:
        draw_grid(stdscr, grid, ball, column)
        if grid.completed:
            stdscr.addstr(*Coord.MESSAGE, "Sorted!")
            stdscr.getch()
            break
        action, column = get_user_input(
            stdscr, column, Asset.POP if state == State.POP else Asset.PUSH
        )
        stack = grid[column]
        if action == Action.QUIT:
            break
        elif action == Action.POP and state == State.POP and not stack.is_empty:
            ball = stack.pop()
            state = State.PUSH
        elif action == Action.PUSH and state == State.PUSH and not stack.is_full:
            stack.push(ball)
            state = State.POP
            ball = " "


def main():
    curses.wrapper(_main)
