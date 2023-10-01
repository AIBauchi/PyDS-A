"""
Author: Swayam

merge_sort.py - A Python implementation of the Merge Sort algorithm for sorting lists.

Merge Sort is a divide-and-conquer algorithm. It divides the unsorted list into n sublists, each containing
one element, and then repeatedly merges sublists to produce new sorted sublists until there is only one sublist remaining.
The main advantage of Merge Sort is its stability and consistent performance.

Resources used:
- https://en.wikipedia.org/wiki/Merge_sort

For doctests run the following command:
python3 -m doctest -v merge_sort.py

For manual testing run:
python3 merge_sort.py
"""

from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list in ascending order using the Merge Sort algorithm.

    Parameters:
        arr (List[int]): The list to be sorted.

    Returns:
        List[int]: The sorted list.

    Examples:
    >>> merge_sort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]

    >>> merge_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    """
    if len(arr) <= 1:
        return arr

    # Divide the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merges two sorted lists into a single sorted list.

    Parameters:
        left (List[int]): The left sorted list.
        right (List[int]): The right sorted list.

    Returns:
        List[int]: The merged sorted list.
    """
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
