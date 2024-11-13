import pytest

from solution import Solution


@pytest.fixture
def median():
    sol = Solution()
    return sol.findMedianSortedArrays


@pytest.mark.parametrize(
    "nums1,nums2,expected",
    [
        pytest.param([1, 3], [2], 2, id="example 1a"),
        pytest.param([2], [1, 3], 2, id="example 1b"),
        pytest.param([1, 2], [3, 4], 2.5, id="example 2a"),
        pytest.param([3, 4], [1, 2], 2.5, id="example 2b"),
        pytest.param([1], [2, 3, 4], 2.5, id="extra 1"),
        pytest.param([], [15], 15.0, id="empty list1"),
        pytest.param([9], [], 9.0, id="empty list2"),
        pytest.param([1] * 1000, [2] * 1000, 1.5, id="max elements"),
    ],
)
def test_median(nums1, nums2, expected, median):
    actual = median(nums1, nums2)
    assert actual == expected
