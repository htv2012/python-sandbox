"""
In an XML file, after locating a node, I want to locate a specific sibbling.
"""

from xml.dom import minidom
doc = minidom.parse('get_sibbling.xml')


for element in doc.getElementsByTagName('skos:prefLabel'):
    print(element.firstChild.data)
    sibbling = element.parentNode.getElementsByTagName('skos:scopeNote')[0]
    print(sibbling.firstChild.data)
