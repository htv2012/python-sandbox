#!/usr/bin/env python3
from term import ask


def main():
    name = ask("What is your name? ", timeout=5)
    print(f"Hello, {name}")


if __name__ == "__main__":
    main()
