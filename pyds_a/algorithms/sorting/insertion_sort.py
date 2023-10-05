"""
Author: Avijit-Dey

insertion_sort.py - A Python implementation of the Insertion Sort algorithm for 
sorting lists.

Insertion sort is a simple sorting algorithm that builds the final 
sorted array (or list) one item at a time by comparisons.
Insertion sort iterates, consuming one input element each repetition, 
and grows a sorted output list. At each iteration, insertion sort removes
one element from the input data, finds the location it belongs within the 
sorted list, and inserts it there. It repeats until no input elements remain. 

Resources used:
--https://en.wikipedia.org/wiki/Insertion_sort

For doctests run the following command:
python3 -m doctest -v insertion_sort.py

For manual testing run:
python3 insertion_sort.py
"""


def insertion_sort(arr):
    """
    Sorts a list in ascending order using the Insertion Sort algorithm.

    Parameters:
        arr (list): The list to be sorted.

    Returns:
        list: The sorted list.

    This algorithm has quadratic time complexity & constant auxiliary space complexity.

    Examples:
    >>> insertion_sort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]

    >>> insertion_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]

    >>> insertion_sort([6,5,3,1,8,7,2,4])
    [1, 2, 3, 4, 5, 6, 7, 8]

    """
    # Case when we have only one element in the array
    if (n := len(arr)) <= 1:
        return

    # Iterating the unsorted part (considering the first element to be sorted)
    for j in range(1, n):
        key = arr[j]
        i = j - 1

        # Performing checks with the first element of the unsorted part
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        # When above condition fails, the key is finally put in its rightful place
        arr[i + 1] = key

    return arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
