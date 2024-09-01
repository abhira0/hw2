"""Module with very intense sorting :p. I'm kidding, its just mergesort!"""


def merge_sort(array: list[int]) -> list[int]:
    """Sort the given array using the algorithm mergesort."""
    if not array:
        return array
    if len(array) == 1:
        return array

    half = len(array)//2

    return recombine(merge_sort(array[:half]), merge_sort(array[half:]))


def recombine(left_arr: list[int], right_arr: list[int]) -> list[int]:
    """By taking two arrays, merge the sort by actually implementing the mergesort algorithm."""
    left_index = 0
    right_index = 0
    merge_arr = [0] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + i] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merge_arr[i + right_index] = left_arr[i]

    return merge_arr
