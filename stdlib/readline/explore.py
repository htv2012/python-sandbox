#!/usr/bin/env python

import readline
import logging

logging.basicConfig(filename='explorer.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def completer(text, state):
    logger.debug("text: {}, state: {}".format(text, state))

def input_loop():
    print('Try out the readline completion, enter q to quit')
    line = ''
    while line != 'q':
        line = input('>')
        print('    ==> %r' % line)


if __name__ == '__main__':
    readline.set_completer(completer)
    readline.set_completer_delims(' ')
    readline.parse_and_bind('tab: complete')
    print('completion type:', readline.get_completion_type())
    input_loop()
