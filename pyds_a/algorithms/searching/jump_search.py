"""
Author: matt-wisdom

jump_search.py - A Python implementation of the Jump Search algorithm.

This script provides a pure Python implementation of the Jump Search algorithm, 
which is used to search for an element in a sorted list or array efficiently. 
The algorithm jumps through blocks of the list to reduce the number of elements 
that need to be checked compared to linear search.

Resources used:
- https://en.wikipedia.org/wiki/Jump_search

Usage:
1. Import the `jump_search` function.
2. Create a sorted list or array.
3. Call `jump_search(arr, target)` with the list or array and the target element
 to search for.

"""

import math


def jump_search(arr, target):
    """
    Finds the index of target in a sorted list using jump search algorithm.

    Parameters:
        arr (list): Sorted list of numbers to search.
        target (int): item to find

    Returns:
        int: Index of target in arr

    Examples:
        >>> arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        >>> target = 11
        >>> result = jump_search(arr, target)
        >>> result
        5
        >>> target = 8
        >>> result = jump_search(arr, target)
        >>> result
        -1
    """
    n = len(arr)
    # Finding the jump size
    step = int(math.sqrt(n))
    prev = 0
    # Jump through the blocks
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        # If reached or gone beyond the end of the array, the target is not present
        if prev >= n:
            return -1
    while arr[prev] < target:
        prev += 1

        # If we've reached the next block or the end of the array,
        # the target is not present
        if prev == min(step, n):
            return -1
    # If the element is found, return its index
    if arr[prev] == target:
        return prev
    return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
