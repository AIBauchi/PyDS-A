"""
Author: Tinny-Robot

binary_search.py - A Python implementation of the binary search algorithm.

This script provides a Python function for performing binary search in a sorted list or array.
The binary_search function takes a sorted list and a target value as input and returns the
index of the target value if found, or -1 if not found.
"""
from functools import lru_cache

@lru_cache
def binary_search(arr, target):
    """
    Perform binary search to find the target value in a sorted list.

    Args:
        arr (list): The sorted list to search within.
        target: The value to search for.

    Returns:
        int: The index of the target value if found, or -1 if not found.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
