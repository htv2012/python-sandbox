#!/usr/bin/env python
import re


def tokenize(expression):
    symbols = ["\\" + symbol for symbol in list("()+-*/")]
    digits = [r"\-{0,1}\d+"]
    pattern = "(" + "|".join(digits + symbols) + ")"
    expression = "(" + expression + ")"
    return re.findall(pattern, expression)


if __name__ == "__main__":
    print(tokenize("(2 + 16) * (45 - 15) / -12"))
    # RPN: 2 16 + 45 15 - * -12 /
