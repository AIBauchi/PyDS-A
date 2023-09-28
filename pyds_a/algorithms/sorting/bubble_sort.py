"""
Author: Tinny-Robot

bubble_sort.py - A Python implementation of the Bubble Sort algorithm for sorting lists.

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, 
compares adjacent elements, and swaps them if they are in the wrong order. 
The pass through the list is repeated until the list is sorted.

Resources used:
- https://en.wikipedia.org/wiki/Bubble_sort

For doctests run the following command:
python3 -m doctest -v bubble_sort.py

For manual testing run:
python3 bubble_sort.py
"""
from functools import lru_cache

@lru_cache
def bubble_sort(arr):
    """
    Sorts a list in ascending order using the Bubble Sort algorithm.

    Parameters:
        arr (list): The list to be sorted.

    Returns:
        list: The sorted list.

    Examples:
    >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]

    >>> bubble_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    """
    number_of_elements = len(arr)
    for i in range(number_of_elements):
        # Flag to optimize the algorithm
        swapped = False

        # Last i elements are already sorted, so no need to compare them again
        for j in range(0, number_of_elements - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break

    return arr

if __name__ == "__main__":
    import doctest

    doctest.testmod()
