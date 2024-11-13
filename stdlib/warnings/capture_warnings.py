
import warnings
from warnings_tryout import set_level


if __name__ == '__main__':
    with warnings.catch_warnings(record=True) as w:
        set_level(-5)
        # print('Message:', w[0].message)
