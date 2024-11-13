"""
Tests for `_split_fields(text, separator)`
"""
from hvtext.kv import _split_fields


def test_colon_as_separator():
    """ Colon as separator should work """
    expected = ['name', 'Karen Carpenter']
    actual = _split_fields('name: Karen Carpenter\n', ':')
    assert expected == actual


def test_equal_as_separator():
    """ Equal sign as separator should work """
    expected = ['name', 'Karen Carpenter']
    actual = _split_fields('name = Karen Carpenter\n', '=')
    assert expected == actual


def test_split_once():
    """ Should split only once """
    expected = ['name', 'Karen:Carpenter']
    actual = _split_fields('name : Karen:Carpenter\n', ':')
    assert expected == actual


def test_space_as_separator():
    """ Using space as separator """
    expected = ['name', 'Karen Carpenter']
    actual = _split_fields('name Karen Carpenter\n', ' ')
    assert expected == actual

