#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
import os
import random
import sys


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


def seed(seed_value=None):
    """Set and remember the seed value"""
    global _inst

    if seed_value is None:
        # seed_value = long(time.time() * 256)
        seed_value = random.randint(0, sys.maxsize)
    _inst.seed(seed_value)
    _inst.seed_value = seed_value
    logger.debug('Seed value: %r', _inst.seed_value)


def get_seed():
    """Return the saved seed value"""
    global _inst
    return _inst.seed_value

_inst = random.Random()
seed()
random = _inst.random
uniform = _inst.uniform
triangular = _inst.triangular
randint = _inst.randint
choice = _inst.choice
randrange = _inst.randrange
sample = _inst.sample
shuffle = _inst.shuffle
normalvariate = _inst.normalvariate
lognormvariate = _inst.lognormvariate
expovariate = _inst.expovariate
vonmisesvariate = _inst.vonmisesvariate
gammavariate = _inst.gammavariate
gauss = _inst.gauss
betavariate = _inst.betavariate
paretovariate = _inst.paretovariate
weibullvariate = _inst.weibullvariate
getstate = _inst.getstate
setstate = _inst.setstate
jumpahead = _inst.jumpahead
getrandbits = _inst.getrandbits
