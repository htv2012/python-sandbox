from typing import Any

import pysnooper


def _up(index: int) -> int:
    return (index - 1) // 2


def _left(index: int) -> int:
    return index * 2 + 1


def _right(index: int) -> int:
    return index * 2 + 2


def _out_of_order(data: list, parent: int, child: int) -> bool:
    try:
        return data[parent] > data[child]
    except IndexError:
        return False


def push(data: list, element: Any):
    data.append(element)

    index = len(data) - 1
    parent = _up(index)
    while index > 0 and data[parent] > data[index]:
        data[index], data[parent] = data[parent], data[index]
        index, parent = parent, _up(parent)


def _heapify_down(data: list, here: int):
    length = len(data)
    while here < length:
        left, right = _left(here), _right(here)
        if left >= length:
            # No children
            break

        if right >= length or data[left] < data[right]:
            child = left
        else:
            child = right
        if data[here] > data[child]:
            data[here], data[child] = data[child], data[here]
            here = child


def pop(data: list) -> Any:
    result = data[0]
    data[0] = data.pop()
    _heapify_down(data, here=0)
    return result


data = [5, 1, 6, 2, 3, 7, 9]
print("\n# Original")
print(data)

print("\n# Heapified")
_heapify_down(data, 0)
print(data)

result = pop(data)
print(f"{result=}, {data=}")
