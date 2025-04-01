#!/usr/bin/env python
# encoding: utf-8
"""
Determines how many file handles we can use before running into error
"""


def get_max_file_handles():
    handles = []
    try:
        for i in range(10000):
            handles.append(open(__file__))
    except IOError:
        pass
    finally:
        max_handles = len(handles)
        for handle in handles:
            handle.close()
    return max_handles


if __name__ == "__main__":
    print("System allow maximum of {0} file handles".format(get_max_file_handles()))
