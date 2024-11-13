#!/usr/bin/env python
"""
Find node "<points>Mr</points>" and change the text
"""
import os
from xml.etree import ElementTree


if __name__ == '__main__':
    data_filename = os.path.join(os.path.dirname(__file__), 'data.xml')
    tree = ElementTree.parse(data_filename)
    root = tree.getroot()

    print('Original XML:')
    ElementTree.dump(tree)
    print('---')

    search_term = 'Mr'
    replacement = 'Monsieur'
    print('Replace {!r} with {!r}:'.format(search_term, replacement))

    points = root.iter('points')
    for node in points:
        if node.text == search_term:
            node.text = 'Monsieur'
            ElementTree.dump(tree)
            break
    else:
        print('Node not found')
