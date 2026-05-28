# sandbox.py
import curses
import curses

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)



def main(screen: curses.window):
    screen.clear()
    screen.addstr(1, 1, "SORT COLOR BALLS")
    screen.refresh()
    screen.getkey()

if __name__=="__main__":
    curses.wrapper(main)