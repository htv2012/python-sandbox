#!/usr/bin/env python
import argparse
from pprint import pprint, pformat


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    action = parser.add_subparsers(dest="action")
    action.required = True

    encode_parser = action.add_parser("encode")
    encode_parser.add_argument("-k", "--key")

    decode_parser = action.add_parser("decode")
    decode_parser.add_argument("-k", "--key")
    decode_parser.add_argument("-f", "--force", action="store_true", default=False)

    parser2 = argparse.ArgumentParser()
    parser2.add_argument("infile")
    parser2.add_argument("outfile")
    parser2.add_argument("-f", "--format")
    parser2.add_argument("-v", "--verbose")

    pprint(parser2._optionals._actions)

    with open("explore_parser_object.txt", "w") as handle:
        handle.write("parser:\n")
        handle.write(pformat(vars(parser), indent=4))
        handle.write("\n")
        handle.write("-" * 80)
        handle.write("\n")
        handle.write("parser2 = ")
        handle.write(pformat(vars(parser2), indent=4))
