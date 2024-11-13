#!/usr/bin/env python3
from tree import Tree, vertical, top_view, bottom_view


if __name__ == '__main__':
    root = Tree.from_iterable([100, 50, 20, 50, 500, 400, 300, 200])

    print("Tree:")
    root.print()
    print('- ' * 20)

    columns = vertical(root)
    print(f'Top View: ', end='')
    print(', '.join(str(element) for element in top_view(root)))
    print('Bottom View: ', end='')
    print(', '.join(str(element) for element in bottom_view(root)))

