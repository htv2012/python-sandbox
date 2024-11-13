#!/usr/bin/env python3
"""
A Python skeleton script
"""
import code
import pathlib
import readline

HIST_FILE = pathlib.Path(__file__).with_name("console-history.txt")


class Controller:
    def __init__(self, ip):
        self.ip = ip

    def __repr__(self) -> str:
        return f"Controller(ip={self.ip!r})"

def main():
    """ Entry """
    # Read the history
    try:
        readline.read_history_file(HIST_FILE)
    except FileNotFoundError:
        pass

    ctrl = Controller("10.0.0.5")
    con = code.InteractiveConsole(locals=locals())
    for mod in ["os", "json", "pathlib"]:
        con.push(f"import {mod}")
    con.interact(
        banner="Welcome to the Controller interpreter",
        exitmsg="Exiting Controller interpreter"
    )

    # Save history
    readline.write_history_file(HIST_FILE)


if __name__ == "__main__":
    main()

