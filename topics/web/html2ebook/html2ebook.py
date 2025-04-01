# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 17:23:34 2014

@author: haiv
"""

from bs4 import BeautifulSoup

with open("ttk.html") as f:
    doc = BeautifulSoup(f)
