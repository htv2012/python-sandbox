from validate_parameters import validate_parameters


class Level:
    info = 'info'
    debug = 'debug'

@validate_parameters(level=Level)
def log(level, msg):
    print('{}: {}'.format(level, msg))


if __name__ == '__main__':
    log(Level.info, 'Entering test')
    log('debug', 'About to delete X')
    log('warn', 'Crash here')
