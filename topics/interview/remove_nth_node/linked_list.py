class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        values = []
        node = self
        while node:
            values.append(node.val)
            node = node.next
        return f"<ListNode count={len(values)}, nodes={values}>"

    def __iter__(self):
        node = self
        while node is not None:
            yield node.val
            node = node.next

    def __eq__(self, other: object) -> bool:
        me = self
        while me is not None and other is not None and me.val == other.val:
            me = me.next
            other = other.next
        return me is None and other is None

    @classmethod
    def from_iterable(cls, it):
        root = None
        prev = None
        node = None
        for value in it:
            node = cls(value)
            if prev is None:
                root = node
            else:
                prev.next = node
            prev = node
        return root
