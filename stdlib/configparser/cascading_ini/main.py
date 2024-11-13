#!/usr/bin/env python
import argparse
import configparser

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("config", nargs="+")

    args = parser.parse_args()
    c = configparser.ConfigParser()
    for conf in args.config:
        c.read(conf)
