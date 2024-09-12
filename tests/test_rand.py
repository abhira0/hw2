"""testing random array generation."""
from src.rand import random_array


def test_random_array_length():
    """length test."""
    arr = [0, 0, 0, 0, 0]
    result = random_array(arr)
    assert len(result) == 5, "The length of the array is changed."


def test_random_array_elements_are_int():
    """type test."""
    arr = [0, 0, 0, 0, 0]
    result = random_array(arr)
    assert all(isinstance(i, int)
               for i in result), "All elements are not integers."


def test_random_array_elements_in_range():
    """range test."""
    arr = [0, 0, 0, 0, 0]
    result = random_array(arr)
    assert all(
        1 <= i <= 20 for i in result), "Elements should be within the range 1 to 20."
