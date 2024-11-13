#!/usr/bin/env python
class StatePersistence:
    def _check_keys(self):
        sentinel = object()
        if getattr(self, 'keys', sentinel) is sentinel:
            raise AttributeError('Need to define the keys at class level')

    def __getstate__(self):
        self._check_keys()
        return dict((key, getattr(self, key)) for key in self.keys)

    def __setstate__(self, state):
        missing = object()
        for key in self.keys:
            new_value = state.get(key, missing)
            if new_value is not missing:
                setattr(self, key, new_value)

