#!/usr/bin/env python3
"""Prove that ExitStack is reusable."""
import contextlib


def main():
    """Entry"""
    exit_stack = contextlib.ExitStack()

    # First use
    with exit_stack:
        exit_stack.callback(print, "callback1")
        print("Hello")

    # Second use
    with exit_stack:
        exit_stack.callback(print, "callback2")
        print("World")


if __name__ == "__main__":
    main()
