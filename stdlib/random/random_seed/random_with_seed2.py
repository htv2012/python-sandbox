#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
import os
import random
import sys
import time
from binascii import hexlify as _hexlify
from os import urandom as _urandom

__all__ = [
    "betavariate",
    "choice",
    "expovariate",
    "gammavariate",
    "gauss",
    "get_seed",
    "getrandbits",
    "getstate",
    "jumpahead",
    "lognormvariate",
    "normalvariate",
    "paretovariate",
    "randint",
    "random",
    "randrange",
    "sample",
    "seed",
    "setstate",
    "shuffle",
    "triangular",
    "uniform",
    "vonmisesvariate",
    "weibullvariate",
]


log_level = os.environ.get('LOGLEVEL', 'INFO')
logging.basicConfig(level=log_level)
logger = logging.getLogger(__name__)


try:
    int
except NameError:
    long = int

class MyRandom(random.Random):
    def get_seed(self):
        """ Return the seed value """
        return self._seed

    def seed(self, seed_value=None):
        """Initialize internal state from hashable object.

        None or no argument seeds from current time or from an operating
        system specific randomness source if available.

        If seed_value is not None or an int or long, hash(seed_value) is used instead.
        """

        # This block copied from the standard library `random`
        if seed_value is None:
            try:
                # Seed with enough bytes to span the 19937 bit
                # state space for the Mersenne Twister
                seed_value = int(_hexlify(_urandom(2500)), 16)
            except NotImplementedError:
                import time
                self.seed_value = int(time.time() * 256) # use fractional seconds

        super(MyRandom, self).seed(seed_value)
        self.gauss_next = None

        self._seed = seed_value
        logger.debug('Seed set to %r', self._seed)


_instance = MyRandom()
_instance.seed()

seed = _instance.seed
get_seed = _instance.get_seed
random = _instance.random
uniform = _instance.uniform
triangular = _instance.triangular
randint = _instance.randint
choice = _instance.choice
randrange = _instance.randrange
sample = _instance.sample
shuffle = _instance.shuffle
normalvariate = _instance.normalvariate
lognormvariate = _instance.lognormvariate
expovariate = _instance.expovariate
vonmisesvariate = _instance.vonmisesvariate
gammavariate = _instance.gammavariate
gauss = _instance.gauss
betavariate = _instance.betavariate
paretovariate = _instance.paretovariate
weibullvariate = _instance.weibullvariate
getstate = _instance.getstate
setstate = _instance.setstate
jumpahead = _instance.jumpahead
getrandbits = _instance.getrandbits
