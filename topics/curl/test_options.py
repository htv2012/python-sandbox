import curllib as curllib
from curllib import options


def test1():
    assert options() == []


def test2():
    assert options("--silent") == ["--silent"]


def test3():
    assert options("--silent", "--verbose") == ["--silent", "--verbose"]


def test4():
    assert options(request="POST") == ["--request=POST"]


def test5():
    assert options(request="POST", retry=5) == ["--request=POST", "--retry=5"]


def test6():
    assert options(retry=5, retry_max_time=10) == ["--retry=5", "--retry-max-time=10"]
