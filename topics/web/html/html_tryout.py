#!/usr/bin/env python
# -*- coding: utf-8 -*-


from html import HTML

if __name__ == "__main__":
    h = HTML()
    h.span("hello", style="foo")
    print(h)
