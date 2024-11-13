#!/usr/bin/env python

import argparse
import os
import curses
try:
    import cursesmenu
except ImportError:
    print('Please pip install cursesmenu')


def icd(cwd=None):
    global screen
    DONE = 'I am done'
    screen = curses.initscr()
    if cwd is None:
        cwd = os.getcwd()
    while True:
        os.chdir(cwd)
        subdirs = [DONE, '..']
        subdirs.extend(x for x in os.listdir(cwd) if os.path.isdir(x))
        menu = cursesmenu.SelectionMenu(subdirs, title=cwd, show_exit_option=False)
        screen.clear()
        menu.show()

        selected = menu.selected_item.text
        if selected == DONE:
            curses.endwin()
            return cwd

        cwd = os.path.normpath(os.path.join(cwd, selected))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dirname', default=None, nargs='?')
    options = parser.parse_args()

    dirname = icd(options.dirname)
    print('Final dir:', dirname)
