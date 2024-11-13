#!/usr/bin/env python

'''
Get quotes using Yahoo service

Each quote is like this:

AverageDailyVolume = 51403200
Change = -0.134
DaysLow = 37.72
DaysHigh = 38.13
YearLow = 26.26
YearHigh = 38.22
MarketCapitalization = 317.4B
LastTradePriceOnly = 38.021
DaysRange = 37.72 - 38.13
Name = Microsoft Corpora
Symbol = MSFT
Volume = 46183876
StockExchange = NasdaqNM

REFERENCE
http://developer.yahoo.com/yql/console/?q=show%20tables&env=store://datatables.org/alltableswithkeys&debug=true#h=select+*+from+yahoo.finance.quote+where+symbol+in+(%22YHOO%22%2C%22AAPL%22%2C%22GOOG%22%2C%22MSFT%22)
'''

from lxml import etree

def get_node_text(top_node, xpath, default_value=None):
    '''
    Given a node, search that node using an xpath expression. If found, return
    that node's text. If not found, return a default value.
    '''
    node = top_node.find(xpath)
    if node is None:
        return default_value
    else:
        return node.text

if __name__ == '__main__':
    filename = 'samples/quotes.xml'
    url = r'''http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quote%20where%20symbol%20in%20(%22YHOO%22%2C%22AAPL%22%2C%22GOOG%22%2C%22MSFT%22)&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'''
    #url = r'http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quote%20where%20symbol%3D%22msft%22&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
    
    doc = etree.parse(url)

    for quote_node in doc.findall('results/quote'):
        price = get_node_text(quote_node, 'LastTradePriceOnly', '-1.00')
        symbol = get_node_text(quote_node, 'Symbol', '??')
        print('{}: {}'.format(symbol, price))

