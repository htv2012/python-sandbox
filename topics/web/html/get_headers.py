#!/usr/bin/env python
# encoding: utf-8
"""
Example script that scans an HTML file and output the texts for H3 tags
"""

import html.parser


class HeadersParser(html.parser.HTMLParser, object):
    def __init__(self):
        super(HeadersParser, self).__init__()
        self.in_header = False

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "h3":
            self.in_header = True

    def handle_endtag(self, attrs):
        self.in_header = False

    def handle_data(self, data):
        if self.in_header:
            print("{}".format(data))


with open("sample.html") as f:
    html_contents = f.read()

parser = HeadersParser()
parser.feed(html_contents)
