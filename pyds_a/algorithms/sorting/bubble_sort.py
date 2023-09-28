"""
Author: matt-wisdom

bubble_sort.py - A Python implementation of the Bubble Sort algorithm.

This script provides a pure Python implementation of the Bubble Sort algorithm,
which repeatedly steps through the list, compares adjacent elements, and swaps
them if they are in the wrong order. This process is repeated until the entire 
list is sorted.

Resources used:
- https://en.wikipedia.org/wiki/Bubble_sort


For manual testing and demonstration, you can use the script as follows:
python3 bubble_sort.py
"""


def bubble_sort(arr):
    """
    Sorts a list in ascending order using the Bubble Sort algorithm.

    Parameters:
        arr (list): The list of elements to be sorted.

    Returns:
        None: The input list is sorted in-place.

    Examples:
        >>> arr = [64, 25, 12, 22, 11]
        >>> bubble_sort(arr)
        >>> arr
        [11, 12, 22, 25, 64]
    """
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    import doctest

    doctest.testmod()
