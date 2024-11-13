#!/usr/bin/env python3
"""
How to use a function which takes one single argument in place of type
"""


import argparse


def new_yaml_file(arg):
    if arg.endswith((".yml", ".yaml")):
        return arg
    else:
        return "{}.yaml".format(arg)


def main():
    """ Entry """
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", type=new_yaml_file, default="default.yaml")

    print(parser.parse_args(["-y", "foo.yml"]))  # 'foo.yml'
    print(parser.parse_args(["-y", "foo.yaml"]))  # 'foo.yaml'
    print(parser.parse_args(["-y", "bar"]))  # 'bar.yaml'
    print(parser.parse_args([]))  # None


if __name__ == "__main__":
    main()
