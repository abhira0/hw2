"""Testcases for the file hw2_debugging."""
from src.hw2_debugging import merge_sort
from src.rand import random_array

def test_hardcoded_array():
    """Array here is hardcoded."""
    arr = [4, 9, 1, 4, 56, -1, 100, -1000, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    merge_sorted_array = merge_sort(arr)
    assert merge_sorted_array == sorted(arr), "Array is not sorted"

def test_random_array():
    """Array here is random."""
    arr = random_array([None] * 20)
    merge_sorted_array = merge_sort(arr)
    assert merge_sorted_array == sorted(arr), "Array is not sorted"

def test_sorted_array():
    """Array here is hardcoded."""
    arr = [-10000000,-100,-3, -2, -1, 0, 1,2,3,100,10000000]
    merge_sorted_array = merge_sort(arr)
    assert merge_sorted_array == sorted(arr), "Array is not sorted"

def test_empty_array():
    """Array here is empty."""
    arr = []
    merge_sorted_array = merge_sort(arr)
    assert merge_sorted_array == sorted(arr), "Array is not sorted"

def test_singleton_array():
    """Array here is single element array."""
    arr = [0]
    merge_sorted_array = merge_sort(arr)
    assert merge_sorted_array == sorted(arr), "Array is not sorted"

def test_uniform_array():
    """Array here is full of 0's."""
    arr = [0] * 10
    merge_sorted_array = merge_sort(arr)
    assert merge_sorted_array == sorted(arr), "Array is not sorted"

def test_only_negatives_array():
    """Array here is full of negative integers."""
    arr = [-i for i in range(1, 11)]
    merge_sorted_array = merge_sort(arr)
    assert merge_sorted_array == sorted(arr), "Array is not sorted"
