#!/usr/bin/env python
import argparse
import xmlrpc.client


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=8000)
    parser.add_argument('server')
    parser.add_argument('amount', type=float)
    arguments = parser.parse_args()

    proxy = xmlrpc.client.ServerProxy('http://%s:%d/' % (arguments.server, arguments.port))
    tip_amount = proxy.tip(arguments.amount)

    print('Sub-total: ${}'.format(arguments.amount))
    print('Tip: ${}'.format(tip_amount))
