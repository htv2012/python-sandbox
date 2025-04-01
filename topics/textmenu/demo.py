#!/usr/bin/env python

# A little program to demo the use of textmenu.menu()

import textmenu

if __name__ == "__main__":
    choices = [
        "Fish",
        "Cut bait",
        "Spear",
        "Mend nets",
        "Dry fish",
        "Dry squid",
        "Make fishsauce",
        "Make shrimp paste",
        "Sell catch",
        "Trade",
    ]
    response = textmenu.menu("What to do?", choices)
    print("You picked choice {!r}".format(response))
