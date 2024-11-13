#!/usr/bin/env python3


def main():
    """Entry"""
    print("without walrus")
    name = input("Enter name: ")
    while name != "q":
        print(f"Hello, {name}")
        name = input("Enter name: ")

    print("---\nWith walrus")
    while (name := input("Enter name: ")) != "q":
        print(f"Hello {name}")


if __name__ == "__main__":
    main()
