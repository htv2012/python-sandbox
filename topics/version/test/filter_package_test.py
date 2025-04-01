import io
import textwrap

from hamcrest import assert_that, equal_to

from version import filter_package


def test_filter_blank_lines():
    lines = ["  ", "", "\t"]
    assert_that(list(filter_package(lines)), equal_to([]))


def test_filter_comments():
    lines = ["# hello", " # hello", "\t#hello"]
    assert_that(list(filter_package(lines)), equal_to([]))


def test_filter_dash():
    lines = ["-h", " --foo", "\t-bar"]
    assert_that(list(filter_package(lines)), equal_to([]))


def test_real_world():
    lines = io.StringIO(
        textwrap.dedent("""
        # Comment 1
        ipython

        # Comment 2
        jupyter >= 1.0
        pudb > 2019.1

        --some-flag

        pycodestyle
        pylint
        pyqt5
        pysnooper
    """)
    )

    expected = [
        "ipython\n",
        "jupyter >= 1.0\n",
        "pudb > 2019.1\n",
        "pycodestyle\n",
        "pylint\n",
        "pyqt5\n",
        "pysnooper\n",
    ]

    assert_that(list(filter_package(lines)), equal_to(expected))
