import random

def mergeSort(arr):
    # Base case: if the array has only one element, it's already sorted
    if len(arr) <= 1:
        return arr

    # Find the midpoint of the array
    half = len(arr) // 2

    # Recursively split the array into two halves and sort them
    left_sorted = mergeSort(arr[:half])
    right_sorted = mergeSort(arr[half:])

    # Merge the two sorted halves
    return recombine(left_sorted, right_sorted)

def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(leftArr) + len(rightArr))

    # Merge the two arrays while both have elements to compare
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
            leftIndex += 1
        else:
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]
            rightIndex += 1

    # Copy any remaining elements from the left array
    while leftIndex < len(leftArr):
        mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
        leftIndex += 1

    # Copy any remaining elements from the right array
    while rightIndex < len(rightArr):
        mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]
        rightIndex += 1

    return mergeArr

# Function to generate a random array of integers (you had a typo with rand)
def random_array(size):
    return [random.randint(0, 100) for _ in range(size)]

# Generate a random array of size 20
arr = random_array(20)

# Sort the array using mergeSort
arr_out = mergeSort(arr)

# Print the sorted array
print(arr_out)