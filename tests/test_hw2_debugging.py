import pytest
from src.hw2_debugging import merge_sort


def test_merge_sort_empty():
    assert merge_sort([]) == []


def test_merge_sort_single_element():
    assert merge_sort([42]) == [42]


def test_merge_sort_multiple_elements():
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [
        1, 1, 2, 3, 4, 5, 5, 6, 9]


if __name__ == "__main__":
    pytest.main()
