#!/usr/bin/env python3
import contextlib


@contextlib.contextmanager
def myfile():
    print("Enter myfile")
    yield
    print("Exit myfile")


class MyResource:
    def __enter__(self):
        print("Enter MyResource")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit MyResource")


def main():
    print("Enter stack")
    with contextlib.ExitStack() as exit_stack:
        exit_stack.callback(print, "Callback")
        exit_stack.enter_context(myfile())
        exit_stack.enter_context(MyResource())
        print("Hello, world")
    print("Exit stack")


if __name__ == '__main__':
    main()

