#!/usr/bin/env python

import readline
import logging


logging.basicConfig(filename='example1.log', level=logging.DEBUG)


class SimpleCompleter(object):
    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        logging.debug('text: %r, state: %r' % (text, state))
        response = None
        if state == 0:
            # First time for this text
            if text:
                self.matches = [
                    s
                    for s in self.options
                    if s and s.startswith(text)
                ]
                logging.debug('%r matches: %r', text, self.matches)
            else:
                self.matches = self.options[:]
                logging.debug('<empty input> matches: %r', self.matches)

        # Return the state'th item from the match list
        # if we have that many
        try:
            response = self.matches[state]
        except IndexError:
            response = None

        return response


def input_loop():
    print('Try out the readline completion, enter q to quit')
    line = ''
    while line != 'q':
        line = input('>')
        print('    ==> %r' % line)


if __name__ == '__main__':
    readline.set_completer(
        SimpleCompleter(['start', 'stop', 'list', 'print']).complete
    )
    readline.set_completer_delims(' ')
    readline.parse_and_bind('tab: complete')

    input_loop()
