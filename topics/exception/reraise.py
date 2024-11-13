#!/usr/bin/env python
def do_something():
    i = 5;
    j = 0;
    k = i / j

if __name__ == '__main__':
    try:
        do_something()
    except RuntimeError as e:
        print('Reraising')
        raise e
