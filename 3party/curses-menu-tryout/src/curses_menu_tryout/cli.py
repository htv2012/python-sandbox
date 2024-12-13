import pathlib
import time

import cursesmenu


def select():
    root = pathlib.Path("~/Sync/snip-data").expanduser()
    names = [path.relative_to(root) for path in root.rglob("*")]

    return cursesmenu.CursesMenu.get_selection(names)


def main():
    print("Hello")
    time.sleep(2)

    selection = select()
    time.sleep(2)
    print(f"Selection={selection!r}")
