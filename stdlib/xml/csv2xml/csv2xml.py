#!/usr/bin/env python

from xml.etree import ElementTree as ET
import csv

with open('users.csv') as input_file, open('users.xml', 'wb') as output_file:
    dict_reader = csv.DictReader(input_file)
    root_node = ET.Element('users')
    for user in dict_reader:
        print(user)
        user_node = ET.SubElement(root_node, 'user')
        for tag, value in list(user.items()):
            ET.SubElement(user_node, tag).text = value

    output_file.write(ET.tostring(root_node))
