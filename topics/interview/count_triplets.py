#!/usr/bin/env python3
import logging
import os
from collections import defaultdict
from itertools import product


logging.basicConfig(level=os.getenv('LOGLEVEL', logging.WARN))
logger = logging.getLogger(__name__)


def count_triplets(li, factor):
    d = defaultdict(list)
    for index, element in enumerate(li):
        d[element].append(index)

    logger.debug('d = %r', d)

    count = 0
    for element in li:
        logger.debug('\n\nelement=%r', element)

        index_list1 = d[element]
        index_list2 = d[element * factor]
        index_list3 = d[element * factor * factor]
        logger.debug('index lists=%r, %r, %r', index_list1, index_list2, index_list3)

        for i in index_list1:
            for j in index_list2:
                for k in index_list3:
                    if i < j < k:
                        count += 1
                        logger.debug('+ %r, %r, %r', i, j, k)
                    else:
                        logger.debug('- %r, %r, %r', i, j, k)

    return count


def main():
    li = [1, 9, 3, 3, 9, 7, 27, 3]
    factor = 3
    print('count triplets of {}, with factor {} is {}'.format(li, factor, count_triplets(li, factor)))

if __name__ == '__main__':
    main()
