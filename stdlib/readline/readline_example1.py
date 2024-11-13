#!/usr/bin/env python

import readline

logger = open('readline.log', 'w')
def my_completer(text, state):
    words = ['setthis', 'setthat', 'set_foo', 'set_ bar', 'ls', 'less', 'bash']
    candidates = [w for w in words if w.startswith(text)] + [None]
    logger.write('--- text: {!r}, state: {!r}, candidates: {!r}\n'.format(text, state, candidates))
    logger.flush()
    return candidates[state]

if __name__ == '__main__':
    history_file = 'history.txt'
    init_file = 'inputrc.txt'

    readline.read_init_file(init_file)
    readline.read_history_file(history_file)
    readline.set_completer(my_completer)

    try:
        print('Testing readline, Ctrl+C to quit')
        while True:
            line = input('> ')
            print(repr(line))
    except KeyboardInterrupt:
        pass
    except EOFError:
        pass
    finally:
        readline.write_history_file(history_file)
