"""this module deals with the algorithm of merge sort."""

def merge_sort(array):
    """This function merges all the sorted array."""
    # Base case: if the array has only one element, it's already sorted
    if len(array) <= 1:
        return array

    # Find the midpoint of the array
    half = len(array) // 2

    # Recursively split the array into two halves and sort them
    left_sorted = merge_sort(array[:half])
    right_sorted = merge_sort(array[half:])

    # Merge the two sorted halves
    return recombine(left_sorted, right_sorted)

def recombine(left_array, right_array):
    """this function recombines two arrays."""
    left_index = 0
    right_index = 0
    merge_array = [None] * (len(left_array) + len(right_array))

    # Merge the two arrays while both have elements to compare
    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            merge_array[left_index + right_index] = left_array[left_index]
            left_index += 1
        else:
            merge_array[left_index + right_index] = right_array[right_index]
            right_index += 1

    # Copy any remaining elements from the left array
    while left_index < len(left_array):
        merge_array[left_index + right_index] = left_array[left_index]
        left_index += 1

    # Copy any remaining elements from the right array
    while right_index < len(right_array):
        merge_array[left_index + right_index] = right_array[right_index]
        right_index += 1

    return merge_array
