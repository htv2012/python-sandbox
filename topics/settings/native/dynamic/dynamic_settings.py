#!/usr/bin/env python
"""

Demo: Dynamically load different configurations at run time

Examples:

    ./dynamic_settings.py settings
    ./dynamic_settings.py settings1
    ./dynamic_settings.py settings2

"""

import argparse


def main():
    """Entry"""
    parser = argparse.ArgumentParser()
    parser.add_argument("settings")
    options = parser.parse_args()
    settings = __import__(options.settings)
    print(settings.server)


if __name__ == "__main__":
    main()
