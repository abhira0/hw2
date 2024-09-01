"""Module with very intense sorting :p. I'm kidding, its just mergesort!"""
import rand


def merge_sort(array):
    """Sort the given array using the algorithm mergesort."""
    if len(array) == 1:
        return array

    half = len(array)//2

    return recombine(merge_sort(array[:half]), merge_sort(array[half:]))


def recombine(left_arr, right_arr):
    """By taking two arrays, merge the sort by actually implementing the mergesort algorithm."""
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            merge_arr[left_index + right_index] = left_arr[left_index]
        else:
            left_index += 1
            merge_arr[left_index + right_index] = right_arr[right_index]

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]

    return merge_arr


arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)
