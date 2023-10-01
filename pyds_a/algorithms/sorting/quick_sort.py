"""
Author: Rajat Gupta

quick_sort.py - A Python implementation of the Quick Sort algorithm for sorting lists.

Quicksort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array 
and partitioning the other elements into two sub-arrays, according to whether they are less than or 
greater than the pivot. For this reason, it is sometimes called partition-exchange sort. 
The sub-arrays are then sorted recursively. This can be done in-place, requiring small additional 
amounts of memory to perform the sorting.

Resources used:
- https://en.wikipedia.org/wiki/Quicksort

For doctests run the following command:
python3 -m doctest -v quick_sort.py

For manual testing run:
python3 quick_sort.py
"""

def quick_sort(arr):
    """
    Sorts a list in ascending order using the Quick Sort algorithm.

    Parameters:
        arr (list): The list to be sorted.

    Returns:
        list: The sorted list.

    Examples:
    >>> quick_sort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]

    >>> quick_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [var_x for var_x in arr if var_x < pivot]
    middle = [var_x for var_x in arr if var_x == pivot]
    right = [var_x for var_x in arr if var_x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    
