#!/usr/bin/env python


class Tag(object):
    def __init__(self, tag_name):
        self._tag_name = tag_name

    def __enter__(self):
        print('<{}>'.format(self._tag_name))
        return self

    def __exit__(self, exception_type, exception_instance, exception_traceback):
        print('</{}>'.format(self._tag_name))
        return False  # False = I do not handle any exception


with Tag('p'):
    print('Lorem ipsum dolor sit amet,')
    print('consectetur adipiscing elit.')

# A different way to accomplish the same thing
print()
tag1 = Tag('p')
tag2 = Tag('b')
with tag1, tag2:
    print('Lorem ipsum dolor sit amet,')
    print('consectetur adipiscing elit.')

