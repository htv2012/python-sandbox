"""
Without the line:
# -*- coding: utf-8 -*-
Write will fail
"""

with open('out.txt', 'wb') as f:
    f.write('Hải')
