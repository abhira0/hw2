"""Module with very intense sorting :p. I'm kidding, its just mergesort!"""
import src.rand as rand


def merge_sort(array):
    """Sort the given array using the algorithm mergesort."""
    if len(array) == 1:
        return array
    print(array)

    half = len(array)//2

    return recombine(merge_sort(array[:half]), merge_sort(array[half:]))


def recombine(left_arr, right_arr):
    """By taking two arrays, merge the sort by actually implementing the mergesort algorithm."""
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        print(f"while inside before: {merge_arr=}, {left_index=}, {right_index=}")
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1
        print(f"while inside after: {merge_arr=}, {left_index=}, {right_index=}")

    for i in range(right_index, len(right_arr)):
        print(f"rightie {i=} {merge_arr=}")
        merge_arr[left_index + i] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        print(f"leftie {i=} {merge_arr=}")
        merge_arr[i + right_index] = left_arr[i]

    print(f"{merge_arr=}")
    return merge_arr


arr = rand.random_array([None] * 10)
arr = [9, 7, 11, 3, 13, 17, 8, 17, 4, 7]
arr_out = merge_sort(arr)

print(arr_out)
