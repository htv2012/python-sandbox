import xml.etree.ElementTree as et

if __name__ == '__main__':
    with open('data.xml') as f:
        doc = et.parse(f)
        for article in doc.findall('article'):
            filename = article.find('title').text + '.xml'
            with open(filename, 'w') as out:
                xml_string = et.tostring(article) + '\n'
                out.write(xml_string)
