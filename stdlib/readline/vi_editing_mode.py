#!/usr/bin/env python
import readline

readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')

print('vi editing mode')
print('Enter q to quit')
while True:
    line = input('> ')
    if line == 'q':
        break
    print('==>', repr(line), '\n')
