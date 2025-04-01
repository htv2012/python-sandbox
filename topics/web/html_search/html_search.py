#!/usr/bin/env python

from bs4 import BeautifulSoup

if __name__ == "__main__":
    b = None
    with open("data.html") as f:
        b = BeautifulSoup(f)
        for td in b.find_all("td"):
            print(td)
            print("")
