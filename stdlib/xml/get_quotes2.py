# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/haiv/.spyder2/.temp.py
"""

#import cgi
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
from lxml import etree


def node2quote(node):
    symbol = node.find('Symbol').text
    price = node.find('LastTradePriceOnly').text
    return symbol, float(price)

def q(symbols):
    '''
    Takes a single or list of stock symbols and return a Yahoo Query Language
    (YQL) statement to retrieve quote information for those symbols.
    '''
    if type(symbols) is list:
        symbols = '","'.join(symbols)
    yql = r'select * from yahoo.finance.quote where symbol in ("{}")'.format(symbols)
    return yql

def g(symbols):
    '''
    Takes a single or list of stock symbols and return the current- or last-
    closed prices.
    '''

    # Build the URL to retrieve data
    query = {
        'q': q(symbols),
        'env': 'store://datatables.org/alltableswithkeys',
    }
    query = urllib.parse.urlencode(query)
    url = 'http://query.yahooapis.com/v1/public/yql?{}'.format(query)
    print(url)

    # Make the API call and process the response
    doc = etree.parse(url)
    return [node2quote(node) for node in doc.findall('results/quote')]

if __name__ == '__main__':
    symbols = 'YHOO AAPL GOOG MSFT'.split()
    symbols = 'csco msft aapl'.split()
    for symbol, price in g(symbols):
        print('{}: {}'.format(symbol, price))
