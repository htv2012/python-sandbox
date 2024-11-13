#!/usr/bin/env python
"""
Test the `kv.parse(iterable, separator='=')` function
"""
from hvtext.kv import parse


def test_default_separator():
    """ Parse using the default separator """
    expected = dict(a='1', b='2')
    actual = parse('a=1;b=2'.split(';'))
    assert expected == actual


def test_explicit_default_separator():
    """ Explicitly specify the default separator """
    expected = dict(a='1', b='2')
    actual = parse('a=1;b=2'.split(';'), '=')
    assert expected == actual


def test_trim_white_spaces():
    """ The parser should trim off white spaces """
    expected = dict(a='1', b='2')
    actual = parse('  a = 1   ;  b = 2 '.split(';'), '=')
    assert expected == actual

def test_should_skip_blank_lines():
    """ The parser should skip the blank lines """
    expected = dict(a='1', b='2')
    actual = parse(';;a: 1;;b: 2;;'.split(';'), ':')
    assert expected == actual


def test_should_skip_comment():
    """ The parser should skip comment lines """
    expected = dict(a='1', b='2')
    actual = parse('# comment1;;a = 1;# comment2;b = 2'.split(';'))
    assert expected == actual


def test_parse_blank_text():
    """ The parser should handle empty text gracefully """
    expected = {}
    actual = parse('')
    assert expected == actual

