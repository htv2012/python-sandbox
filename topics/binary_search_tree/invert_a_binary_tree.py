#!/usr/bin/env python
# My solution to inverting a binary tree


from tree import BinarySearchTree


def main():
    #      4                    4
    #     /  \                 /  \
    #    /    \               /    \
    #   2      6     ==>     6      2
    #  / \    / \           / \    / \
    # 1   3  5   7         7   5  3   1
    tree = BinarySearchTree.from_sequence('4261357')

    print(' '.join(tree.in_order_traversal()))
    print(' '.join(tree.pre_order_traversal()))

    tree.invert()
    print('---')

    print(' '.join(tree.in_order_traversal()))
    print(' '.join(tree.pre_order_traversal()))

if __name__ == '__main__':
    main()
