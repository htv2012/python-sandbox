#!/usr/bin/env python3
"""
app1.py
Print text in reversed
"""

while (input_text := input("> ")) != "q":
    print(input_text[::-1])
