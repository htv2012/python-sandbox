#!/usr/bin/env python

# Read/parse an XML file using etree

from lxml import etree

def get_node_text(top_node, xpath, default_value=None):
    node = top_node.find(xpath)
    if node is None:
        return default_value
    else:
        return node.text

if __name__ == '__main__':
    filename = 'samples/config_with_attributes.xml'
    doc = etree.parse(filename)

    # Print the attributes of the root node
    print('CONFIG', end=' ')
    for k,v in list(doc.getroot().items()):
        print('{}={}'.format(k,v), end=' ')
    print('')

    # Print information in the <server> node
    host = get_node_text(doc, 'server/host')
    port = get_node_text(doc, 'server/port', '8899')
    primary = get_node_text(doc, 'server/primary', default_value='No')
    print('  Host: {}'.format(host))
    print('  Port: {}'.format(port))
    print('  Primary: {}'.format(primary))

    # Print the <users> node
    print('  Users')
    for tag in ['prefix', 'start', 'count', 'password']:
        node_value = get_node_text(doc, 'users/{}'.format(tag))
        print('    {}: {}'.format(tag, node_value))

    # Print the <scenarios>
    print('  Scenarios')
    for scenario in doc.findall('scenarios/scenario'):
        print('    ID: {},'.format(scenario.get('id')), end=' ')
        print('src: {}'.format(scenario.get('src')))
        for tag in ['max_users_count', 'secured_login', 'use_smtp', 'exit_on_first_error']:
            node_value = get_node_text(scenario, tag, '<none>')
            print('      {}: {}'.format(tag, node_value))
