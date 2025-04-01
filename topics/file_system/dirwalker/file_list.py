#!/usr/bin/env python

import os


class FileList(object):
    def __init__(self, root):
        self._root = root
        self.clear_cache()
        self.caching_hook = None

    def clear_cache(self):
        self._cache = []
        self._cache_status = "not cache"

    def __iter__(self):
        if self._cache_status == "cached":
            for fullpath in self._cache:
                yield fullpath
        else:
            for dirpath, dirnames, filenames in os.walk(self._root):
                for filename in filenames:
                    fullpath = os.path.join(dirpath, filename)
                    self._cache.append(fullpath)
                    self._cache_status = "caching"
                    if callable(self.caching_hook):
                        self.caching_hook(fullpath)
                    yield fullpath
            self._cache_status = "cached"
