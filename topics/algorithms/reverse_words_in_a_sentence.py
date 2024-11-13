#!/usr/bin/env python
def revstring(s):
    l = list(s)
    l.reverse()
    return "".join(l)


def revwords(s):
    l = s.split()
    l.reverse()
    return " ".join(l)


s = "Ask, and you might get it."
print(s)
print(revstring(s))
print(revwords(s))
