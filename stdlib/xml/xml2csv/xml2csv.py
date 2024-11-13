#!/usr/bin/env python

"""
xml2csv.py
by Hai Vu
Convert an XML file to csv
"""

import csv
import io
import xml.sax

xml_data = """
<orders>
    <order customer="john" product="eggs" quantity="12" />
    <order customer="cindy" product="bread" quantity="1" />
    <order customer="larry" product="tea bags" quantity="100" />
    <order customer="john" product="butter" quantity="1" />
    <order product="chicken" quantity="2" customer="derek" />
</orders>
""".strip()


class OrdersHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.rows = []

    def startElement(self, name, attributes):
        if name != "order":
            return

        self.rows.append(
            {name: attributes.getValue(name) for name in sorted(attributes.getNames())}
        )


def main():
    print("\n# XML:")
    print(xml_data)

    handler = OrdersHandler()
    xml.sax.parseString(xml_data, handler)

    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=handler.rows[0])
    writer.writerows(handler.rows)

    print("\n# CSV:")
    print(buffer.getvalue())


if __name__ == "__main__":
    main()
