#!/usr/bin/env python

import marshal
import types


def greet(name):
    print('Hello, {}'.format(name))

if __name__ == '__main__':
    # Save the code into a file
    with open('greet_marshal.txt', 'w') as f:
        code_string = marshal.dumps(greet.__code__)
        f.write(code_string)

    # Read the code from file
    with open('greet_marshal.txt') as f:
        greet_code = marshal.loads(f.read())
        hello = types.FunctionType(greet_code, globals())
        hello('Hai')
