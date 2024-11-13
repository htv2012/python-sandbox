from typing import Iterable


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


def from_iterable(it: Iterable) -> ListNode:
    root = None
    prev = None
    node = None
    for value in it:
        node = ListNode(value)
        if prev is None:
            root = node
        else:
            prev.next = node
        prev = node
    return root
