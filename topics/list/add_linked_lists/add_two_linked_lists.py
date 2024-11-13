#!/usr/bin/env python
"""
Given two linked lists representing the digits from two numbers, write
an add function to return a linked list representing the sum.
"""




class Node(object):
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return 'Node({!r}, {!r})'.format(self.data, self.__next__)

    def __str__(self):
        return '{}'.format(self.data)


class List(object):
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.length = 0
        for item in iterable or []:
            self.append(item)

    def prepend(self, data):
        self.length += 1
        new_node = Node(data, self.head)
        self.head = new_node

    def append(self, data):
        self.length += 1
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.__next__

    def __str__(self):
        buffer = ' '.join(str(node) for node in self)
        return buffer

    def __len__(self):
        return self.length


def add(list1, list2):
    it1 = iter(list1)
    it2 = iter(list2)

    reversed_sum = List()  # Reversed sum
    length_difference = len(list1) - len(list2)
    for _ in range(length_difference):
        reversed_sum.prepend(it1.next().data)
    for _ in range(-length_difference):
        reversed_sum.prepend(it2.next().data)

    for node1, node2 in zip(it1, it2):
        reversed_sum.prepend(node1.data + node2.data)

    print('Reversed sum: {}'.format(reversed_sum))
    sum_list = List()
    carry = 0
    for node in reversed_sum:
        value = node.data + carry
        value, carry = value % 10, value // 10
        sum_list.prepend(value)
    if carry:
        sum_list.prepend(carry)
    return sum_list


# test
list1 = List([2, 7])
list2 = List([9, 8, 5])
sum_list = add(list1, list2)

print('{} + {} = {}'.format(list1, list2, sum_list))
