#!/usr/bin/env python
"""
Find node "Header" and change the text
https://stackoverflow.com/a/51932287/459745
"""
from __future__ import print_function
import os
from xml.etree import ElementTree


if __name__ == '__main__':

    #
    # Method 1
    #
    tree = ElementTree.parse('messages.xml')
    root = tree.getroot()

    for elem in root:
        for subelem in elem:
            if 'RequestNo' in subelem.tag:
                subelem.text = '41194813'
                break

    # Register the namespace so when we save to the file, the output is
    # free of "ns0:" prefixes
    ElementTree.register_namespace('', 'URL/sampleMessages-v1')

    tree.write('messages-new.xml')

    #
    # Method 2
    #

    # tree = ElementTree.parse('messages.xml')
    # root = tree.getroot()

    # namespaces = {'xxx': 'URL/sampleMessages-v1'}
    # node = root.find('xxx:Header/xxx:RequestNo', namespaces)

    # if node is not None:
    #     node.text = '41194813'

    # print()
    # print('Modified XML:')
    # ElementTree.dump(root)

