import pytest
from src.rand import random_array


def test_random_array_length():
    arr = [0, 0, 0, 0, 0]  # Initial array
    result = random_array(arr)
    assert len(result) == 5, "The length of the array should not change."


def test_random_array_elements_are_int():
    arr = [0, 0, 0, 0, 0]  # Initial array
    result = random_array(arr)
    for element in result:
        assert isinstance(element, int), "All elements should be integers."


def test_random_array_elements_in_range():
    arr = [0, 0, 0, 0, 0]  # Initial array
    result = random_array(arr)
    for element in result:
        assert 1 <= element <= 20, "Elements should be within the range 1 to 20."


if __name__ == "__main__":
    pytest.main()
