#!/usr/bin/env python3
from tree import Tree, bottom_view, top_view, vertical

if __name__ == "__main__":
    root = Tree.from_iterable([100, 50, 20, 50, 500, 400, 300, 200])

    print("Tree:")
    root.print()
    print("- " * 20)

    columns = vertical(root)
    print("Top View: ", end="")
    print(", ".join(str(element) for element in top_view(root)))
    print("Bottom View: ", end="")
    print(", ".join(str(element) for element in bottom_view(root)))
