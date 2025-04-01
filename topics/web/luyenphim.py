#!/usr/bin/env python

import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from optparse import OptionParser

from sgmllib import SGMLParser


class LuyenPhimExtract(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.urls = []

    def start_a(self, attributes):
        href_list = [v for k, v in attributes if k == "href"]
        if len(href_list) > 0:
            href = href_list[0]
        else:
            href = ""

        pattern = "^.*(http://www.megaupload.com\/\?d=[A-Za-z0-9]*)$"
        searchResult = re.match(pattern, href)
        if searchResult:
            # os.system('open ' + searchResult.group(1))
            self.urls.append(searchResult.group(1))


def string_to_int(string, value_if_empty, last):
    if string == "":
        return value_if_empty
    elif string in ["end", "last", "$"]:
        return last

    try:
        int_value = int(string)
        if int_value < 0:
            int_value = last + int_value
        return int_value
    except ValueError:
        print("Error: invalid number: " + string)
        sys.exit(3)


def parse_range(range, last):
    SEPARATOR = ","
    if range.find(SEPARATOR) == -1:
        print("Error: range must be in format start,end")
        sys.exit(2)

    start, end = range.split(",")
    start = string_to_int(start, 1, last)
    end = string_to_int(end, last, last)

    if start > end:
        return end, start
    else:
        return start, end


def download(url, options):
    sock = urllib.request.urlopen(url)
    htmlSource = sock.read()
    sock.close()

    parser = LuyenPhimExtract()
    parser.feed(htmlSource)

    url_count = len(parser.urls)
    if options.range == "all":
        download_start = 1
        download_end = url_count
    else:
        download_start, download_end = parse_range(options.range, url_count)
    # print 'start: %d, end: %d' % (download_start, download_end)

    for i in range(download_start - 1, download_end):
        print("%s" % (parser.urls[i]))
        if options.do_download:
            os.system("open " + parser.urls[i])


def parser_command_line():
    usage = "Usage %prog [options] URL"
    parser = OptionParser(
        usage=usage,
        version="%prog 1.1",
        description="Download megaupload videos from a URL",
    )
    parser.add_option(
        "-n",
        "--noop",
        dest="do_download",
        default=True,
        action="store_false",
        help="No download, only show the links",
    )  # user name
    parser.add_option(
        "-r",
        "--range",
        dest="range",
        default="all",
        action="store",
        help="Select links to download, e.g. -r 1,5",
    )
    options, args = parser.parse_args()
    if len(args) != 1:
        parser.print_help()
        sys.exit(1)

    return options, args[0]


def main():
    options, url = parser_command_line()
    download(url, options)


if __name__ == "__main__":
    main()
