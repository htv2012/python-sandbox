# sandbox.py
import curses

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)


def _main(screen: curses.window):
    screen.clear()
    screen.addstr(1, 1, "SORT COLOR BALLS")
    screen.refresh()
    screen.getkey()

def main():
    curses.wrapper(_main)