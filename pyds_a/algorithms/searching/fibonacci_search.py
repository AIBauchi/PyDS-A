"""
Author: Tinny-Robot

fibonacci_search.py - A Python implementation of the Fibonacci search algorithm.

This script provides a pure Python implementation of the Fibonacci search algorithm
for searching an element in a sorted list or array. The Fibonacci search algorithm
uses Fibonacci numbers to divide the search space efficiently.

Resources used:
- https://en.wikipedia.org/wiki/Fibonacci_search_technique

For doctests run the following command:
python3 -m doctest -v fibonacci_search.py

For manual testing run:
python3 fibonacci_search.py
"""

from functools import lru_cache


@lru_cache
def fibonacci(k: int) -> int:
    """
    Finds the Fibonacci number at index k.

    Parameters:
        k (int): Index of the Fibonacci number to find.

    Returns:
        int: Fibonacci number at position k.

    Raises:
        TypeError: If k is not an integer.
        ValueError: If k is negative.

    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(2)
        1
        >>> fibonacci(5)
        5
        >>> fibonacci(15)
        610
        >>> fibonacci('a')
        Traceback (most recent call last):
        TypeError: k must be an integer.
        >>> fibonacci(-5)
        Traceback (most recent call last):
        ValueError: k integer must be greater or equal to zero.
    """
    if not isinstance(k, int):
        raise TypeError("k must be an integer.")
    if k < 0:
        raise ValueError("k integer must be greater or equal to zero.")
    if k == 0:
        return 0
    elif k == 1:
        return 1
    else:
        return fibonacci(k - 1) + fibonacci(k - 2)


def fibonacci_search(arr: list, val: int) -> int:
    """
    A pure Python implementation of the Fibonacci search algorithm.

    Parameters:
        arr (list): List of sorted elements.
        val: Element to search in the list.

    Returns:
        int: The index of the element in the array, or -1 if not found.

    Examples:
        >>> fibonacci_search([4, 5, 6, 7], 4)
        0
        >>> fibonacci_search([4, 5, 6, 7], -10)
        -1
        >>> fibonacci_search([-18, 2], -18)
        0
        >>> fibonacci_search([5], 5)
        0
        >>> fibonacci_search(['a', 'c', 'd'], 'c')
        1
        >>> fibonacci_search(['a', 'c', 'd'], 'f')
        -1
        >>> fibonacci_search([], 1)
        -1
        >>> fibonacci_search([.1, .4 , 7], .4)
        1
        >>> fibonacci_search([], 9)
        -1
        >>> fibonacci_search(list(range(100)), 63)
        63
        >>> fibonacci_search(list(range(100)), 99)
        99
        >>> fibonacci_search(list(range(-100, 100, 3)), -97)
        1
        >>> fibonacci_search(list(range(-100, 100, 3)), 0)
        -1
        >>> fibonacci_search(list(range(-100, 100, 5)), 0)
        20
        >>> fibonacci_search(list(range(-100, 100, 5)), 95)
        39
    """
    len_list = len(arr)
    # Find m such that F_m >= n where F_i is the i-th Fibonacci number.
    i = 0
    while True:
        if fibonacci(i) >= len_list:
            fibb_k = i
            break
        i += 1
    offset = 0
    while fibb_k > 0:
        index_k = min(
            offset + fibonacci(fibb_k - 1), len_list - 1
        )  # Prevent out of range
        item_k_1 = arr[index_k]
        if item_k_1 == val:
            return index_k
        elif val < item_k_1:
            fibb_k -= 1
        elif val > item_k_1:
            offset += fibonacci(fibb_k - 1)
            fibb_k -= 2
        else:
            return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
