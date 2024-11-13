#!/usr/bin/env python
from typed_input import int_input, float_input

if __name__ == '__main__':
    value = int_input('Int Value: ')
    print('Value is {}'.format(value))

    value = float_input('Float: ')
    print('Value is', value)
