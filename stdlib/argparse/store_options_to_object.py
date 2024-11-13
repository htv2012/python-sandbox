#!/usr/bin/env python
"""
Demo storing options to an object

Example arguments:

    -i 5
    -b
    -b -i19

Why do we want to use a custom class?
- Because we can
- To provide extra data (via class- or instance attributes)
- to provide extra functionality (via methods)
"""
import argparse
import dataclasses


@dataclasses.dataclass
class Options:
	boolval: bool = False
	intval: int = -1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--intval", type=int)
    parser.add_argument("-b", "--boolval", action="store_true")

    options = Options()
    parser.parse_args(namespace=options)
    print(options)