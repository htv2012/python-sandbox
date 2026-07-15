#!/usr/bin/env python3
import argparse
import curses
import itertools
import random
import time


class Snail:
    def __init__(self, win, name, row, col, target):
        self.win = win
        self.name = name
        self.row = row
        self.col = col
        self.target = target
        self.draw()
        self.draw_name()
        self.draw_target()

    def draw(self):
        self.win.addstr(self.row, self.col, "@v")
        self.win.refresh()

    def draw_name(self):
        self.win.addstr(self.row, 1, self.name)

    def draw_target(self):
        self.win.addstr(self.row, self.target, "|")

    def erase(self):
        self.win.addstr(self.row, self.col, "..")

    def advance(self, step):
        if step == 0:
            return
        self.erase()
        self.col += 1
        self.draw()


def create_runners(win, names, target):
    rows = itertools.count(5)
    runners = [Snail(win, name, next(rows), 10, target) for name in names]
    return runners


def get_command_line_options():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-r",
        "--runners",
        help="names of runners, separated by space, keep them < 9 letters long",
        nargs="*",
        default=["Slimmy", "Squishy"],
    )
    parser.add_argument(
        "-t",
        "--target",
        help="Column number of the target",
        default=30,
        type=int,
    )
    options = parser.parse_args()
    return options


def main(stdscr):
    options = get_command_line_options()
    curses.curs_set(0)
    stdscr.clear()
    stdscr.addstr(1, 1, "S N A I L S   R A C E")
    stdscr.refresh()

    names = options.runners
    random.shuffle(names)
    snails = create_runners(stdscr, names, options.target)
    winner = None
    while winner is None:
        snail = random.choice(snails)
        snail.advance(1)
        if snail.col == options.target:
            winner = snail
            break
        time.sleep(1.0 / len(snails))

    stdscr.addstr(2, 1, f"The winner is {winner.name}")
    stdscr.addstr(3, 1, "Press any key to continue")
    stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)
