"""
Append multiple flags
"""

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-DOverride", dest="overrides", action="append")

    args = ["-DOverride=one", "-DOverride=two,three", "-DOverride=four"]
    options = parser.parse_args(args)

    print("Options:", options)
