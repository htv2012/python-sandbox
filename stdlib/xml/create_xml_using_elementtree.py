#!/usr/bin/env python

import xml.etree.ElementTree as ET
import xml.dom.minidom


def create_book_node(parent, attributes=None, **kwargs):
    book_node = ET.SubElement(parent, 'book')

    if attributes:
        book_node.attrib = attributes

    if kwargs:
        for tag, value in list(kwargs.items()):
            node = ET.SubElement(book_node, tag)
            node.text = value


def main():
    # Create XML from a skeleton
    skeleton = '''<books>
    <description>My Books List</description>
    <owner>Hai Vu</owner>
    </books>'''
    root = ET.fromstring(skeleton)

    # Add books
    create_book_node(
        root,
        attributes={'isbn': '9780062024039'},
        title='Divergent',
        author='Veronica Roth')
    create_book_node(
        root,
        attributes={'isbn': '9780062024046'},
        title='Insurgent',
        author='Veronica Roth')
    create_book_node(
        root,
        attributes={'isbn': '9780062024060'},
        title='Allegiant',
        author='Veronica Roth')

    # xml.etree.ElementTree does not provide pretty printing, minidom does
    xml_string = ET.tostring(root, 'utf-8')
    doc = xml.dom.minidom.parseString(xml_string)
    print(doc.toprettyxml())


if __name__ == '__main__':
    main()