"""
Author: Raghav Sharma (rghvsh)
mergesort.py - A Python implementation of the Merge Sort algorithm for sorting lists.
Merge sort is a general purpose and comparison based algorithm
Conceptually, a merge sort works as follows:
Divide the unsorted list into n sublists, each containing one element
(a list of one element is considered sorted).Repeatedly merge sublists
to produce new sorted sublists until there is only one sublist remaining.
This will be the sorted list.
Resources used:
- https://en.wikipedia.org/wiki/Merge_sort
For doctests run the following command:
python -m doctest -v mergesort.py
For manual testing run:
python mergesort.py -v
"""

def merge_two_sorted_arrarys(a, b):
    """
         Merges the elements of two sorted arrays in such a way that the output array is in ascending order.
         Parameters:
             a (list): First sorted list to be merged.
             b (list): Second sorted list to be merged.
         Returns:
             list: The merged and sorted list.
         Examples:
         >>> merge_two_sorted_arrarys([1, 3, 7, 9],[2, 4, 6, 8])
         [1, 2, 3, 4, 6, 7, 8, 9]
         >>> merge_two_sorted_arrarys([11, 13, 14, 34],[7, 9, 12, 24])
         [7, 9, 11, 12, 13, 14, 24, 34]
    """
    array = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            array.append(a[i])
            i = i + 1

        else:
            array.append(b[j])
            j = j+1

    while i < len(a):
        array.append(a[i])
        i = i+1

    while j < len(b):
        array.append(b[j])
        j = j + 1

    return array


def merge_sort(arr):
    """
         Sorts a list in ascending order using the Merge Sort algorithm.
         Parameters:
             arr (list): The list to be sorted.
         Returns:
             list: The sorted list.
         Examples:
         >>> merge_sort([64, 34, 25, 12, 22, 11, 90])
         [11, 12, 22, 25, 34, 64, 90]
         >>> merge_sort([5, 4, 3, 2, 1])
         [1, 2, 3, 4, 5]
    """

    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = arr[mid:]
    right = arr[:mid]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_arrarys(left, right)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
