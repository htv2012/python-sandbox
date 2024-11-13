import xml.etree.ElementTree as et


class XmlResponse(object):
    """ A simple class to parse a response XML """
    def parse_string(self, xml_string):
        """
        Parses an XML block of text and convert all secondary nodes into
        attributes for this object.
        """
        root = et.fromstring(xml_string)
        for node in root:
            setattr(self, node.tag, node.text)

    def __init__(self, filename):
        """
        Parses an XML file and convert all secondary nodes into
        attributes for this object.
        """
        with open(filename) as f:
            self.parse_string(f.read())


def interpret_response(filename):
    """ A simple demo of how to use the XMLResponse class """
    print('\n{}:'.format(filename))

    response = XmlResponse(filename)
    if response.status == 'ok':
        print('Job ID:', response.jobid)
    else:
        print('Error:', response.error)

if __name__ == '__main__':
    interpret_response('ok.xml')
    interpret_response('fail.xml')
