#!/usr/bin/env python3
"""Explitcitly close an ExitStack."""
import contextlib


@contextlib.contextmanager
def make_vm(name):
    print(f"create vm {name}")
    yield name
    print(f"cleanup vm {name}")


class TestBed:
    def __init__(self, *names):
        print("create testbed")
        self.exit_stack = contextlib.ExitStack()
        # self.exit_stack.__enter__()
        for name in names:
            self.exit_stack.enter_context(make_vm(name))
    
    def __del__(self):
        self.exit_stack.close()
        print("cleanup testbed")

def main():
    tb = TestBed("Alex", "Kim", "Karen")


if __name__ == '__main__':
    main()
