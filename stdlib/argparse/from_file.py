#!/usr/bin/env python3

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(fromfile_prefix_chars="@")
    parser.add_argument("-s", "--server", default="foo")
    parser.add_argument("-p", "--port", default=3306, type=int)

    args = parser.parse_args(["@from_file.txt"])
    print(args)
