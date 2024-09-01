"""Module containing code to generate random array."""
import subprocess


def random_array(arr: list[int]):
    """Function that returns random elements in an array by using 'shuf' cli tool."""
    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=False)
        arr[i] = int(shuffled_num.stdout)
    return arr
