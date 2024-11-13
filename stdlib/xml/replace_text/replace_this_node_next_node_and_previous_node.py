#!/usr/bin/env python
"""
Find node "<points>Mr</points>", change this node and the next
"""
import os
import re
from xml.etree import ElementTree


if __name__ == '__main__':
    data_filename = os.path.join(os.path.dirname(__file__), 'data.xml')
    tree = ElementTree.parse(data_filename)
    root = tree.getroot()

    appelation = re.compile('Mr')
    points = root.iter('points')
    nodes_stack = []
    for node in points:
        if appelation.match(node.text):
            # Modify this node
            node.text = 'Monsieur'

            # Modify next node
            next_node = next(points)
            next_node.text = 'Francois'

            # Modify previous node
            previous_node = nodes_stack.pop()
            previous_node.text = 'modified'
            # Keep popping the stack the get to previous nodes
            # in reversed order

            ElementTree.dump(root)
            break
        else:
            nodes_stack.append(node)
