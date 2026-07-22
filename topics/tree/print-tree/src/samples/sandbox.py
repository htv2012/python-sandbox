import argparse
import pathlib

from print_tree import print_tree

parser = argparse.ArgumentParser()
parser.add_argument("root", type=pathlib.Path)
args = parser.parse_args()

assert args.root.is_dir()
print_tree(args.root)
