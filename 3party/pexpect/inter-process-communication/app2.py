#!/usr/bin/env python3
"""
app2.py
Reverse each words
"""

while (text := input("> ")) != "q":
    words = [word[::-1] for word in text.split()]
    print(" ".join(words))
