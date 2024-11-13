#!/usr/bin/env python


import cmd
import shlex


class MyCmd(cmd.Cmd):
    prompt = '> '
    intro = 'type help for a list of valid commands, Ctrl+D to exit'

    def do_add(self, arguments):
        """ add - Adds two numbers the print the sum""" 
        sum_value = sum(float(x) for x in shlex.split(arguments))
        return sum_value

    def do_shell(self, arguments):
        # print('Shell: "{}"'.format(arguments))
        return 'under construction'

    def do_EOF(self, s):
        """ quit - quit the program""" 
        return True

    def postcmd(self, stop, line):
        print(stop)
        return stop is True

if __name__ == '__main__':
    cmd = MyCmd()
    cmd.cmdloop()
    print('\nBye')
