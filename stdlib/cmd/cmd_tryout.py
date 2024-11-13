#!/usr/bin/env python


import cmd
import shlex


class MyCmd(cmd.Cmd):
    prompt = '> '
    intro = 'type help for a list of valid commands, Ctrl+D to exit'

    def do_add(self, arguments):
        '''add - Adds two numbers the print the sum'''
        x, y = shlex.split(arguments)
        x, y = int(x), int(y)
        print(x + y)

    def do_append(self, arguments):
        print('under construction')
        
    def do_shell(self, arguments):
        print('Shell: "{}"'.format(arguments))

    def do_EOF(self, s):
        '''quit - quit the program'''
        return True

if __name__ == '__main__':
    cmd = MyCmd()
    cmd.cmdloop()
    print('\nBye')
