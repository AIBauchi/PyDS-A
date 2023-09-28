"""
Author: Tinny-Robot

linear_search.py - A Python implementation of the linear search algorithm.

This script provides a pure Python implementation of the linear search algorithm,
which is used to search for a target element in a given list or sequence.

For doctests, run the following command:
python3 -m doctest -v linear_search.py

For manual testing, run:
python3 linear_search.py
"""


def linear_search(sequence: list, target: int) -> int:
    """
    A pure Python implementation of a linear search algorithm.

    Args:
        sequence (list): A collection with comparable items (no sorting required).
        target (int): The item value to search for.

    Returns:
        int: The index of the found item or -1 if the item is not found.

    Examples:
        >>> linear_search([0, 5, 7, 10, 15], 0)
        0
        >>> linear_search([0, 5, 7, 10, 15], 15)
        4
        >>> linear_search([0, 5, 7, 10, 15], 5)
        1
        >>> linear_search([0, 5, 7, 10, 15], 6)
        -1
    """
    for index, item in enumerate(sequence):
        if item == target:
            return index
    return -1


def rec_linear_search(sequence: list, low: int, high: int, target: int) -> int:
    """
    A pure Python implementation of a recursive linear search algorithm.

    Args:
        sequence (list): A collection with comparable items (no sorting required).
        low (int): Lower bound of the search range.
        high (int): Upper bound of the search range.
        target (int): The element to be found.

    Returns:
        int: The index of the found key or -1 if the key is not found.

    Examples:
        >>> rec_linear_search([0, 30, 500, 100, 700], 0, 4, 0)
        0
        >>> rec_linear_search([0, 30, 500, 100, 700], 0, 4, 700)
        4
        >>> rec_linear_search([0, 30, 500, 100, 700], 0, 4, 30)
        1
        >>> rec_linear_search([0, 30, 500, 100, 700], 0, 4, -6)
        -1
    """
    if not (0 <= high < len(sequence) and 0 <= low < len(sequence)):
        raise Exception("Invalid upper or lower bound!")
    if high < low:
        return -1
    if sequence[low] == target:
        return low
    if sequence[high] == target:
        return high
    return rec_linear_search(sequence, low + 1, high - 1, target)


if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n").strip()
    sequence = [int(item.strip()) for item in user_input.split(",")]

    target = int(input("Enter a single number to be found in the list:\n").strip())
    result = linear_search(sequence, target)
    if result != -1:
        print(f"linear_search({sequence}, {target}) = {result}")
    else:
        print(f"{target} was not found in {sequence}")
