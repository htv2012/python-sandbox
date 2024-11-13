#!/usr/bin/env python
import readline

readline.read_init_file('readline.rc')

print('vi editing mode')
print('Enter q to quit')
while True:
    line = input('> ')
    if line == 'q':
        break
    print('==>', repr(line), '\n')
