#!/usr/bin/env python
# encoding: utf-8
"""
etree_tryout.py
Try out the Python's etree
Created by Hai Vu on 2010-02-27.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os

try:
    from lxml import etree
    print("running with lxml.etree")
except ImportError:
    try:
        # Python 2.5+
        import xml.etree
        import xml.etree.cElementTree as etree
        print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # Python 2.5
            import xml.etree.ElementTree as etree
            print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree
                print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree
                    print("running with ElementTree")
                except ImportError:
                    print("Failed to import ElementTree from any known place")

def printNode(node, level=0, indent='    '):
    output = indent * level + node.tag
    if node.text.strip() != '':
        output += ' = '
        output += node.text
        
    # Process attributes
    attributes = list(node.items())
    if len(attributes) != 0:
        output += '('
        output += ', '.join(['%s="%s"' % (k,v) for k,v in attributes])
        output += ')'
        
    print(output)
    level += 1
    for childNode in node:
        printNode(childNode, level, indent)

def xmlNodeToDict(node):
    d = {}

    # Process all attributes
    for k, v in list(node.items()):
        d['@' + k] = v

    childrenNodes = []
    for childNode in node:
        if childNode.getchildren() == []:
            #print('  %s = %s' % (childNode.tag, childNode.text))
            d[childNode.tag] = childNode.text
        childrenNodes.append(xmlNodeToDict(childNode))
    if childrenNodes != []:
        d[node.getchildren()[0].tag] = childrenNodes
    return d

def main():
    xmlfile = '../samples/config_with_attributes.xml'
    xmlfile = '/Users/haiv/temp/addresses3.xml'
    doc = etree.parse(xmlfile)
    root = doc.getroot()
    print((xmlNodeToDict(root)))


if __name__ == '__main__':
	main()

