#!/usr/bin/env python
from xmlrpc.server import SimpleXMLRPCServer
import argparse
import logging
import os
import platform
import socket
import subprocess


logging.basicConfig(level=os.getenv('LOGLEVEL', logging.WARN))
logger = logging.getLogger(__name__)


def calculate_tip(amount):
    tip = amount * 0.15
    print('tip({}) ==> {}'.format(amount, tip))
    return tip


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', default=8000, type=int)
    parser.add_argument('address')
    arguments = parser.parse_args()

    server = SimpleXMLRPCServer((arguments.address, arguments.port))
    logger.debug('Listening on http://%s:%d', *server.server_address)
    server.register_function(calculate_tip, 'tip')
    server.serve_forever()
