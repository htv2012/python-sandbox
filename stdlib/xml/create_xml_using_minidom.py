#!/usr/bin/env python

import xml.dom.minidom


def create_node(xml_document, tag, value=None):
    node = xml_document.createElement(tag)
    if value:
        text_node = xml_document.createTextNode(value)
        node.appendChild(text_node)
    return node


def add_book(xml_document, attributes=None, **kwargs):
    book_node = create_node(xml_document, 'Book')

    if attributes:
        for k, v in list(attributes.items()):
            book_node.setAttribute(k, v)

    for k, v in list(kwargs.items()):
        node = create_node(xml_document, k, v)
        book_node.appendChild(node)

    xml_document.documentElement.appendChild(book_node)

if __name__ == '__main__':
    skeleton = '<Books><Description>My Books List</Description><Owner>Hai Vu</Owner></Books>'
    xml_document = xml.dom.minidom.parseString(skeleton)

    add_book(
        xml_document,
        attributes={'isbn': '9780062024039'},
        title='Divergent',
        author='Veronica Roth')
    add_book(
        xml_document,
        attributes={'isbn': '9780062024046'},
        title='Insurgent',
        author='Veronica Roth')
    add_book(
        xml_document,
        attributes={'isbn': '9780062024060'},
        title='Allegiant',
        author='Veronica Roth')

    print(xml_document.toprettyxml(indent='    '))
