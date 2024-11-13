import xml.etree.ElementTree as ET

if __name__ == '__main__':
    with open('debug.log') as f:
        doc = ET.parse(f)

        for country in doc.findall('.//country'):
            for neighbor in country.findall('neighbor'):
                country.remove(neighbor)

        ET.dump(doc)  # Display

