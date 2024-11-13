# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 17:15:07 2013

@author: haiv

http://stackoverflow.com/questions/20085508/python-how-to-parse-prop-name-elements-in-xml

Read and parse attributes from an XML file using ElementTree

"""

import xml.etree.ElementTree as ET

doc = ET.parse('test.xml')
xpath_expression = (
    'FileTemplate/properties/'
    'obj[@name="GeneralSettings"]/'
    'properties/prop[@name="BufferSize"]')
for prop_node in doc.iterfind(xpath_expression):
    print('Name:', prop_node.get('name'))
    print('Type:', prop_node.get('type'))
    print('Text:', prop_node.text)
