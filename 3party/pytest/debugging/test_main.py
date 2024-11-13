def test_that_need_debugging():
    expected = "things that break".split()
    actual = "things that work".split()
    assert actual == expected
