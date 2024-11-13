#!/usr/bin/env python

import xml.etree.ElementTree as ET
import os
import xml.dom.minidom


def create_node(xml_document, tag, value=None):
    node = xml_document.createElement(tag)
    if value:
        text_node = xml_document.createTextNode(value)
        node.appendChild(text_node)
    return node


def create_dir_node(xml_document, dirpath):
    dir_node = create_node(xml_document, 'FileGroup')

    node = create_node(xml_document, 'Title', os.path.split(dirpath)[-1])
    dir_node.appendChild(node)

    node = create_node(xml_document, 'Description', 'noop')
    dir_node.appendChild(node)

    node = create_node(xml_document, 'Expanded', 'false')
    dir_node.appendChild(node)

    xml_document.documentElement.appendChild(dir_node)
    return dir_node


def create_file_node(xml_document, parent_node, dirpath, filename):
    extension = os.path.splitext(filename)[-1]
    if extension not in ['.jp2']:
        return

    file_node = create_node(xml_document, 'File')

    path_node = create_node(xml_document, 'Path', os.path.join(dirpath, filename))
    file_node.appendChild(path_node)

if __name__ == '__main__':
    skeleton = '<ShoeBox><Version>2011</Version></ShoeBox>'
    xml_document = xml.dom.minidom.parseString(skeleton)
    xml_root = xml_document.documentElement

    CrawlingStartpoint = '/Users/haiv/src/python/xml'
    for dirpath, dirnames, filenames in os.walk(CrawlingStartpoint):
        dir_node = create_dir_node(xml_document, dirpath)
        for filename in filenames:
            file_node = create_file_node(xml_document, dir_node, dirpath, filename)

    print(xml_document.toprettyxml())
