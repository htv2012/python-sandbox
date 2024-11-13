class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"< {self.val} >"
        # values = []
        # node = self
        # while node:
        #     values.append(node.val)
        #     node = node.next
        # return f"<ListNode count={len(values)}, nodes={values}>"

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


def assert_values(head: ListNode, expected: list):
    node = head
    for expected_value in expected:
        assert node.val == expected_value
        node = node.next
    assert node is None
