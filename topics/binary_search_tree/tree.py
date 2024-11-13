class BinarySearchTree(object):
    def __init__(self, data, left_node=None, right_node=None):
        self.data = data
        self.left = left_node
        self.right = right_node

    def __repr__(self):
        return "Tree({})".format(self.data)

    @classmethod
    def from_sequence(cls, sequence):
        data_list = iter(sequence)
        root = cls(next(data_list))
        for data in data_list:
            root.insert(data)
        return root

    def insert(self, data):
        if data < self.data:
            if self.left == None:
                self.left = self.__class__(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right == None:
                self.right = self.__class__(data)
            else:
                self.right.insert(data)

    def in_order_traversal(self):
        if self.left is not None:
            for v in self.left.in_order_traversal():
                yield v
        yield self.data
        if self.right is not None:
            for v in self.right.in_order_traversal():
                yield v

    def pre_order_traversal(self):
        yield self.data
        if self.left is not None:
            for v in self.left.pre_order_traversal():
                yield v
        if self.right is not None:
            for v in self.right.pre_order_traversal():
                yield v

    def invert(self):
        if self.left is not None:
            self.left.invert()

        if self.right is not None:
            self.right.invert()

        self.left, self.right = self.right, self.left


    def lca(self, data1, data2):
        """
        Find the lowest common ancestor
        """
        smaller, larger = sorted([data1, data2])
        print("dbg: data={}, smaller={}, larger={}".format(self.data, smaller, larger))

        print("dbg S({}) <= D({}) <= L({}): {}".format(smaller, self.data, larger, smaller <= self.data <= larger))
        if smaller <= self.data <= larger:
            print("dbg: found: {}".format(self))
            return self

        if larger < self.data:
            print("dbg: go left")
            if self.left:
                return self.left.lca(smaller, larger)
            else:
                return self
        if self.data < smaller:
            if self.right:
                return self.right.lca(smaller, larger)
            else:
                return self
        # elif smaller == self.data or larger == self.data:
        #     return self

def main():
    #      4                    4
    #     /  \                 /  \
    #    /    \               /    \
    #   2      6     ==>     6      2
    #  / \    / \           / \    / \
    # 1   3  5   7         7   5  3   1
    tree = BinarySearchTree.from_sequence('4261357')
    print(tree)

    print(' '.join(tree.in_order_traversal()))
    print(' '.join(tree.pre_order_traversal()))

    # print tree.lca(6, 2)
    # print tree.lca(4, 2)
    print(tree.lca(3, 2))

if __name__ == '__main__':
    main()
