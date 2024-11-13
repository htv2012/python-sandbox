#!/usr/bin/env python3
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer

with open(__file__) as stream:
    code = stream.read()

print(highlight(code, lexer=PythonLexer(), formatter=TerminalFormatter()))
