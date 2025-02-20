#!/usr/bin/env python

import curses

myscreen = curses.initscr()

#myscreen.border(0)
myscreen.addstr(0, 0, "Python curses in action!")
myscreen.refresh()


w = curses.newwin(20, 0, 2, 2)
w.border(0)
w.addstr(5, 5, 'PY is cool')
w.refresh()

ch = myscreen.getch()

curses.endwin()
print(repr(ch))
print(chr(ch))
