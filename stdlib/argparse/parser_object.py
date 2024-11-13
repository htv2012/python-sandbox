#!/usr/bin/env python
import argparse
from pprint import pprint


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    actions = parser.add_subparsers(dest="action")
    actions.required = True

    encode_parser = actions.add_parser("encode")
    encode_parser.add_argument("-k", "--key")

    decode_parser = actions.add_parser("decode")
    decode_parser.add_argument("-k", "--key")
    decode_parser.add_argument("-f", "--force", action="store_true", default=False)

    pprint(vars(parser))
    print("-" * 80)

    parser2 = argparse.ArgumentParser()
    parser2.add_argument("-v", "--verbose")
    parser2.add_argument("filename")
    pprint(vars(parser2))
