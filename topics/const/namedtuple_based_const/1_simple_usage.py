#!/usr/bin/env python
"""
Example of how to use the const package
"""
import const


def main():
    """Entry"""
    DOOR_STATE = const.define(shut=0, locked=1, open=2, ajar=3)
    print("DOOR_STATE:", DOOR_STATE)
    print("ajar:", DOOR_STATE.ajar)


if __name__ == "__main__":
    main()
