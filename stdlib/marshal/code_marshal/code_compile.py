#!/usr/bin/env python


import code

greet_source = '''
def greet(name):
    print 'Hello, {}'.format(name)
'''
greet_code  = code.compile_command(greet_source)
main_source = "greet('world')"

interpreter = code.InteractiveInterpreter()
interpreter.runcode(greet_code)
interpreter.runsource("greet('world')")

