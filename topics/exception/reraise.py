#!/usr/bin/env python3
def do_something():
    i = 5
    j = 0
    return i / j


def main():
    try:
        do_something()
    except RuntimeError as e:
        print("Reraising")
        raise e


if __name__ == "__main__":
    main()
