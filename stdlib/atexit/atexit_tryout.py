#!/usr/bin/env python

import atexit

@atexit.register
def bye():
    print('Goodbye')

if __name__ == '__main__':
    print('You can press Ctrl+C')
    name = input('What is your name? ')
    print('Hello, {}'.format(name))
