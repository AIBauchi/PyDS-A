"""
Author: Tinny-Robot

queue.py - A Python implementation of a queue data structure.

This file contains the implementation of a queue data structure using a list.
A queue follows the First-In-First-Out (FIFO) principle, where the first element added
to the queue is the first one to be removed.

The Queue class provides methods for adding items to the end of the queue, removing items
from the front of the queue, checking if the queue is empty, and getting the current size
of the queue.

Usage:
    from queue import Queue

    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    item = my_queue.dequeue()
    size = my_queue.size()

"""

class Queue:
    """
    Represents a queue data structure implemented using a list.

    A queue follows the First-In-First-Out (FIFO) principle, where the first element added
    to the queue is the first one to be removed.

    Methods:
        enqueue(item): Add an item to the end of the queue.
        dequeue(): Remove and return the item from the front of the queue.
        is_empty(): Check if the queue is empty.
        size(): Get the current size of the queue.
    """

    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.items = []

    def enqueue(self, item):
        """
        Add an item to the end of the queue.

        Args:
            item: The item to be added to the queue.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the item from the front of the queue.

        Returns:
            The item removed from the front of the queue.
        """
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0

    def size(self):
        """
        Get the current size of the queue.

        Returns:
            int: The number of items in the queue.
        """
        return len(self.items)
