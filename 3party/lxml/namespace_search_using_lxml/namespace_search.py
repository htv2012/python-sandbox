"""
https://stackoverflow.com/a/31193631/459745

lxml search will do the right thing without having to declare namespaces.
"""

from lxml import etree as ET

with open("ct.cps", "rb") as stream:
    tree = ET.parse(stream)
ns = {"rdf": "http://foo.bar.com/rdf"}
for constant_node in tree.findall(".//Constant", ns):
    print(constant_node.attrib["key"])
