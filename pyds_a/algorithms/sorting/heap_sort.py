"""
Author: Aharrar Soulali Mohammed

heap_sort.py - A Python implementation of the Heap Sort algorithm for sorting lists.

Heap sort is a comparison-based sorting technique based on Binary Heap Data Structure. 
It can be seen as an optimization over selection sort where we first find the max (or min) element and swap it with the last (or first).
We repeat the same process for the remaining elements. In Heap Sort, we use Binary Heap so that we can quickly find and move the max element in O(Log n) instead of O(n) and hence achieve the O(n Log n) time complexity.

Resources used:
- https://www.geeksforgeeks.org/heap-sort/

For doctests run the following command:
python3 -m doctest -v heap_sort.py

For manual testing run:
python3 heap_sort.py
"""

def heap_sort(arr):
    """
    Sorts a list in ascending order using the Heap Sort algorithm.

    Parameters:
        arr (list): The list to be sorted.

    Returns:
        list: The sorted list.

    Examples:
    >>> heap_sort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]

    >>> heap_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    """
    def heapify(arr, n, i):
        """
        Converts a subtree rooted at index i into a max heap.

        Parameters:
            arr (list): The list representation of the heap.
            n (int): The size of the heap.
            i (int): The root index of the subtree.
        """
        largest = i  # Initialize the largest as root
        left = 2 * i + 1  # Left child index
        right = 2 * i + 2  # Right child index

        # Check if left child exists and is greater than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if right child exists and is greater than the largest so far
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If largest is not root, swap and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap
            heapify(arr, n, largest)

    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[i], arr[0] = arr[0], arr[i]
        # Call heapify on the reduced heap
        heapify(arr, i, 0)

    return arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
