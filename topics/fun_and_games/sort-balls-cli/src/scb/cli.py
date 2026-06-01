# sandbox.py
import curses
import enum
import io

from .asset import Asset
from .generate import create_grid
from .grid import COLUMNS_COUNT, Grid
from .logger import logger
from .stack import EMPTY_VALUE


class State(enum.Enum):
    POP = enum.auto()
    PUSH = enum.auto()


class Coord:
    GRID_TOP_LEFT = (5, 1)
    MESSAGE = (20, 1)


class Action:
    LEFT = ord("h")
    RIGHT = ord("l")
    TOGGLE = ord(" ")
    QUIT = ord("q")


def draw_grid(stdscr: curses.window, grid: Grid, ball: str, ball_column):
    stdscr.clear()
    stdscr.addstr(1, 1, "SORT COLOR BALLS")
    y, x = Coord.GRID_TOP_LEFT

    # Draw the "popped" ball
    stdscr.addstr(y - 1, 3 + (ball_column * 5), ball)

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


def get_user_input(stdscr: curses.window, column: int, cursor: str):
    y = 16
    x = 3 + (column * 5)
    logger.debug(f"get_user_input, {y=}, {x=}, {column=}")
    stdscr.addstr(y, x, cursor)

    while True:
        key = stdscr.getch()
        if key == Action.RIGHT:
            logger.debug(f"Right from {y=}, {x=}, {column=}")
            stdscr.addstr(y, x, " ")
            column = (column + 1) % COLUMNS_COUNT
            x = 3 + (column * 5)
            stdscr.addstr(y, x, cursor)
            logger.debug(f"        to {y=}, {x=}, {column=}")
        elif key == Action.LEFT:
            logger.debug(f"Left from {y=}, {x=}, {column=}")
            stdscr.addstr(y, x, " ")
            column = (column - 1) % COLUMNS_COUNT
            x = 3 + (column * 5)
            stdscr.addstr(y, x, cursor)
            logger.debug(f"       to {y=}, {x=}, {column=}")
        elif key == Action.TOGGLE:
            logger.debug(f"Toggle, {column=}")
            return Action.TOGGLE, column
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
    ball_column = column

    while True:
        draw_grid(stdscr, grid, ball, ball_column)
        if grid.completed:
            stdscr.addstr(*Coord.MESSAGE, "Sorted!")
            stdscr.getch()
            break
        logger.debug(f"Before get_user_input, {column=}, {state=}, {ball=}")
        action, column = get_user_input(
            stdscr, column, Asset.POP if state == State.POP else Asset.PUSH
        )
        logger.debug(f"After get_user_input, {column=}, {action=}")
        stack = grid[column]
        if action == Action.QUIT:
            break
        elif action == Action.TOGGLE:
            if state == State.POP:
                if not stack.is_empty:
                    ball = stack.pop()
                    ball_column = column
                    state = State.PUSH
            elif state == State.PUSH:
                if not stack.is_full:
                    stack.push(ball)
                    state = State.POP
                    ball = " "
                    ball_column = column


def main():
    curses.wrapper(_main)
