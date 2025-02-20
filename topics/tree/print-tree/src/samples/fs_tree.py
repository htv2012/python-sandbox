import argparse
import pathlib

from print_tree import print_tree

parser = argparse.ArgumentParser()
parser.add_argument("root")
options = parser.parse_args()

root = pathlib.Path(options.root)
assert root.is_dir()

print_tree(
    nodes=list(root.glob("*")),
    get_value=lambda p: p.name,
    get_children=lambda p: list(p.glob("*")),
)
