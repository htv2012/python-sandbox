#!/usr/bin/env python

"""
xml2csv_etree.py
by Hai Vu
Convert an XML file to csv using etree
"""

from xml.etree import ElementTree as ET

csv_field_order = ["customer", "product", "quantity"]
xmlfile = "data.xml"
for event, element in ET.iterparse(xmlfile, events=["start"]):
    # you may want to select a specific element.tag here
    if element.tag != "order":
        continue

    # format and print the CSV line to the standard output
    print((",".join(element.attrib.get(title, "") for title in csv_field_order)))
