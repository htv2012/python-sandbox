#!/usr/bin/env python3
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        try:
            for ch in s:
                if ch == "(" or ch == "[" or ch == "{":
                    stack.append(ch)
                elif ch == ")":
                    left = stack.pop()
                    if left != "(":
                        return False
                elif ch == "]":
                    left = stack.pop()
                    if left != "[":
                        return False
                elif ch == "}":
                    left = stack.pop()
                    if left != "{":
                        return False
        except IndexError:
            return False

        return stack == []
