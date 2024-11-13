#!/usr/bin/env python
# encoding: utf-8
"""
bs_tryout1.py

Created by Hai Vu on 2013-03-16.
Copyright (c) 2013 High View Software. All rights reserved.
"""

import sys
import os
from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse

def get_html_source(url):
    response = urllib.request.urlopen(url)
    if response.code != 200:
        print('Failed to open URL: {}'.format(url))
        print('GET returns {}'.format(response.code))
        sys.exit(1)
    return response

def host_filter(tag):
    '''
    Returns True for downloadable media
    '''
    TARGET_HOST = 'ryushare.com'
    return tag.name == 'a' and 'href' in tag and TARGET_HOST in tag.text

if __name__ == '__main__':
    url = 'http://www.phim88.com/forum/threads/17454-Ng%E1%BB%8Dc-T%E1%BB%B7-K%E1%BB%B3-%C3%81n-20-20-FFVN-B%C6%B0%E1%BB%9Bc-Ngo%E1%BA%B7t-Cu%E1%BB%99c-%C4%90%E1%BB%9Di-The-Days-of-Days-TVB-2013-12-20-HD720p-USLT'
    response = get_html_source(url)
    soup = BeautifulSoup(response)
    links = soup.find_all(host_filter)

    previous_file_format = ''
    for link in links:
        file_format = link.find_previous('b').text.strip() # HDTV, HD720p, ...
        episode = link.previous.strip()                    # Tap 1:, Tap 2:, ...
        if file_format != previous_file_format:
            print('')
            print(file_format)
        print('   ', episode, link.text)
        previous_file_format = file_format
