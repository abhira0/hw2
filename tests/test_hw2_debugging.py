"""testing merge sort."""
from src.hw2_debugging import merge_sort
from src.rand import random_array


def test_merge_sort_empty():
    """Array here is empty."""
    arr = []
    assert merge_sort(arr) == sorted(arr), "Array is not sorted"


def test_merge_sort_single_element():
    """Array here is singleton with single element."""
    arr = [42]
    assert merge_sort(arr) == sorted(arr), "Array is not sorted"


def test_merge_sort_multiple_elements():
    """Array here is hardcoded."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert merge_sort(arr) == sorted(arr), "Array is not sorted"


def test_random_array():
    """Array here is random."""
    arr = random_array([0] * 20)
    assert merge_sort(arr) == sorted(arr), "Array is not sorted"


def test_sorted_array():
    """Array here is hardcoded."""
    arr = [-10000000, -100, -3, -2, -1, 0, 1, 2, 3, 100, 10000000]
    assert merge_sort(arr) == sorted(arr), "Array is not sorted"


def test_only_negatives_array():
    """Array here is full of negative integers."""
    arr = [-i for i in range(1, 11)]
    assert merge_sort(arr) == sorted(arr), "Array is not sorted"
