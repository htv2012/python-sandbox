# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 16:38:37 2014

@author: haiv
"""

from xml.dom import minidom

def remove_xml_declaration(xml_text):
    doc = minidom.parseString(xml_text)
    root = doc.documentElement
    xml_text_without_declaration = root.toxml(doc.encoding)
    return xml_text_without_declaration

#
# Test
#
    
xml_text = '''<?xml version="1.0" encoding="UTF-8"?>
<data>
</data>
'''

xml_text = remove_xml_declaration(xml_text)
print(xml_text)
print('---')

xml_text = remove_xml_declaration(xml_text)
print(xml_text)
print('---')

