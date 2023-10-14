"""
Author: Swayam
count_sort.py - A Python implementation of the Count Sort algorithm for sorting lists.
Count Sort is a non-comparison-based sorting algorithm. It works by counting the number of occurrences of each element
in the input list and using that information to reconstruct the sorted list.
Resources used:
- https://en.wikipedia.org/wiki/Counting_sort
For doctests run the following command:
python3 -m doctest -v count_sort.py
For manual testing run:
python3 count_sort.py
"""

from typing import List


def count_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list in ascending order using the Count Sort algorithm.
    Parameters:
        arr (List[int]): The list to be sorted.
    Returns:
        List[int]: The sorted list.
    Examples:
    >>> count_sort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]
    >>> count_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    """
    if not arr:
        return arr

    # Find the range of values in the input list
    min_val = min(arr)
    max_val = max(arr)

    # Create a count array to store the occurrences of each element
    count = [0] * (max_val - min_val + 1)

    # Count the occurrences of each element
    for num in arr:
        count[num - min_val] += 1

    # Reconstruct the sorted list
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i + min_val] * count[i])

    return sorted_arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
