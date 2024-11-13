from lxml import etree

sxlt_doc = etree.parse('addresses.xsl')
transform = etree.XSLT(sxlt_doc)

doc = etree.parse('addresses.xml')
output = transform(doc)

print(output)
