
import warnings


def set_level(level):
    if level < 0:
        warnings.warn('Level should not be negative: {}'.format(level))
        level = 0
    print('Level set to: {}'.format(level))

if __name__ == '__main__':
    set_level(5)
    set_level(-5)
    print('End')
