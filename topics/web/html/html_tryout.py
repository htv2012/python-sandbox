#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
from html import HTML


if __name__ == '__main__':
    h = HTML()
    h.span('hello', style='foo')
    print(h)
