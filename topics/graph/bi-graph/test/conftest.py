import pytest

from bi_graph import BiGraph


@pytest.fixture
def graph():
    return BiGraph()
