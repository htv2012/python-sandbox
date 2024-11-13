#!/usr/bin/env python


import cmd
import shlex


class MyCmd(cmd.Cmd):
    prompt = '> '
    intro = 'type help for a list of valid commands, q to exit'

    def __init__(self, completekey='tab', stdin=None, stdout=None):
        super().__init__(completekey, stdin, stdout)
        if stdin is not None:
            self.use_rawinput = False
            self.prompt = ""
            self.intro = ""

    def do_add(self, arguments):
        '''add - Adds two numbers the print the sum'''
        x, y = shlex.split(arguments)
        x, y = int(x), int(y)
        print(x + y)

    def do_append(self, arguments):
        print('append is under construction')

    def do_shell(self, arguments):
        print('Shell: "{}"'.format(arguments))

    def do_q(self, s):
        '''q - quit the program'''
        return True

    do_EOF = do_q


import io
script = io.StringIO("""add 1 2
shell foo bar
append
""")


if __name__ == '__main__':
    cmd = MyCmd(stdin=script)
    cmd.cmdloop()
    print('\nBye')
