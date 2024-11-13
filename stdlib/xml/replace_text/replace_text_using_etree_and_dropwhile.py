#!/usr/bin/env python
"""
Find node "<points>Mr</points>", change this node and the next
http://stackoverflow.com/a/40306031/459745
"""
import os
import re
from itertools import dropwhile
from xml.etree import ElementTree


if __name__ == '__main__':
    data_filename = os.path.join(os.path.dirname(__file__), 'data.xml')
    tree = ElementTree.parse(data_filename)
    root = tree.getroot()

    appelation = re.compile('Mr')
    points = dropwhile(lambda node: not appelation.match(node.text), root.iter('points'))
    mr_node = next(points)
    mr_node.text = 'Monsieur'
    name_node = next(points)
    name_node.text = 'Francois'

    ElementTree.dump(tree)
