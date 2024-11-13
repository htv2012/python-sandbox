#!/usr/bin/env python

from verifier.verify import verify, msg

def test_eq_with_default_message():
	""" Tests the eq operator with default message """
	verify("foo").eq("bar")

def test_in():
	assert 15 in [1, 2]
	verify(15).in_([1, 2, 3])
