# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 14:09:55 2013

@author: haiv
"""

import bs4

with open('samples/quotes.xml') as f:
    s = bs4.BeautifulSoup(f.read())
