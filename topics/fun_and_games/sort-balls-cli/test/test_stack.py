from scb.data import Stack


def test_empty():
    stack = Stack()
    assert stack.is_empty
    assert not stack.is_full


def test_push_pop():
    stack = Stack()
    for i in range(8):
        stack.push(i)
    assert stack.is_full

    out = []
    while not stack.is_empty:
        out.append(stack.pop())
    assert stack.is_empty
    assert out == [7, 6, 5, 4, 3, 2, 1, 0]
