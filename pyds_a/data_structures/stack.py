"""
Author: Tinny-Robot

stack.py - A Python implementation of a stack data structure.

This file contains the implementation of a stack data structure using a list.
A stack follows the Last-In-First-Out (LIFO) principle, where the last element added
to the stack is the first one to be removed.

The Stack class provides methods for adding items to the top of the stack, removing items
from the top of the stack, checking if the stack is empty, getting the current size
of the stack, and peeking at the item on the top of the stack without removing it.

"""


class Stack:
    """
    Represents a stack data structure implemented using a list.

    A stack follows the Last-In-First-Out (LIFO) principle, where the last element added
    to the stack is the first one to be removed.

    Methods:
        push(item): Add an item to the top of the stack.
        pop(): Remove and return the item from the top of the stack.
        is_empty(): Check if the stack is empty.
        size(): Get the current size of the stack.
        peek(): Return the item at the top of the stack without removing it.
    """

    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.items = []

    def push(self, item):
        """
        Add an item to the top of the stack.

        Args:
            item: The item to be added to the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the item from the top of the stack.

        Returns:
            The item removed from the top of the stack.
        """
        try:
            return self.items.pop()
        except IndexError as exc:
            raise IndexError("Stack is empty") from exc

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def size(self):
        """
        Get the current size of the stack.

        Returns:
            int: The number of items in the stack.
        """
        return len(self.items)

    def peek(self):
        """
        Return the item at the top of the stack without removing it.

        Returns:
            The item at the top of the stack.
        """

        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")
