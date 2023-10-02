"""
Author: Raghav Sharma (rghvsh)

bucket_sort.py - A Python implementation of the Bucket Sort algorithm for sorting lists.

Bucket sort, or bin sort, is a sorting algorithm that works by distributing the elements
of an array into a number of buckets. Each bucket is then sorted individually, either using
a different sorting algorithm, or by recursively applying the bucket sorting algorithm.

Resources used:
- https://en.wikipedia.org/wiki/Bucket_sort

For doctests run the following command:
- python -m doctest -v bucket_sort.py

For manual testing run:
- python bucket_sort.py -v
"""


def bucket_sort(array):
    """
           Sorts a list in ascending order using the Bucket Sort algorithm.

           Parameters:
               arr (list): The list to be sorted.
           Returns:
               list: The sorted list.

           Examples:
           >>> bucket_sort([64, 34, 25, 12, 22, 11, 90])
           [11, 12, 22, 25, 34, 64, 90]
           >>> bucket_sort([5, 4, 3, 2, 1])
           [1, 2, 3, 4, 5]
           >>> bucket_sort([2, 45, 21, 34, 67, 88, 64, 78])
           [2, 21, 34, 45, 64, 67, 78, 88]
           >>> bucket_sort([4, 7, 2, 5, 4, 6, 1, 78, 44, 56, 90, 87, 65])
           [1, 2, 4, 4, 5, 6, 7, 44, 56, 65, 78, 87, 90]

      """
    largest = max(array)
    length = len(array)
    size = largest / length

    buckets = [[] for i in range(length)]

    for i in range(length):
        index = int(array[i] / size)
        if index != length:
            buckets[index].append(array[i])
        else:
            buckets[length - 1].append(array[i])

    for i in range(len(array)):
        buckets[i] = sorted(buckets[i])

    result = []
    for i in range(length):
        result = result + buckets[i]

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
