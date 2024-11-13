import pytest

from tree import Tree


@pytest.fixture(scope="class")
def single_node():
    tree = Tree("Hello")
    return tree


class TestSingleNode:
    def test_verify_value(self, single_node):
        assert single_node.value == "Hello"

    def test_verify_parent(self, single_node):
        assert single_node.parent is None


@pytest.fixture(scope="class")
def two_tier() -> Tree:
    root = Tree("root")
    for i in range(1, 4):
        Tree(f"Child {i}", parent=root)
    return root


class TestTwoTier:
    def test_verify_count(self, two_tier):
        children = list(two_tier.iter_children())
        assert len(children) == 3

    def test_verify_values(self, two_tier):
        actual = [node.value for node in two_tier.iter_children()]
        assert actual == ["Child 1", "Child 2", "Child 3"]

    def test_verify_parent(self, two_tier: Tree):
        for child in two_tier.iter_children():
            assert child.parent is two_tier


@pytest.fixture(scope="class")
def tadd():
    root = Tree("root")
    child1 = Tree("child1")
    child2 = Tree("child2")
    root.add_children(child1, child2)
    return root


class TestAdd:
    def test_verify_count(self, tadd):
        children = list(tadd.iter_children())
        assert len(children) == 2

    def test_verify_parent(self, tadd):
        children = list(tadd.iter_children())
        assert children[0].parent is tadd
        assert children[1].parent is tadd
