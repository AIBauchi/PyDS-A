"""
Author: Tinny-Robot

This module defines a simple singly linked list data structure with basic operations like
adding nodes, removing nodes, searching for a specific value, and displaying the list's contents.
"""


class Node:
    """
    Represents a node in a singly linked list.

    Attributes:
        data: The data stored in the node.
        next: Reference to the next node in the linked list.
    """

    def __init__(self, data):
        """
        Initialize a new Node with the given data.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next = None

    def get_data(self):
        """
        Get the data stored in the node.

        Returns:
            The data stored in the node.
        """
        return self.data

    def set_data(self, data):
        """
        Set the data in the node to a new value.

        Args:
            data: The new data value to be stored in the node.
        """
        self.data = data


class LinkedList:
    """
    Represents a singly linked list data structure.

    The LinkedList class provides basic operations for working with a linked list,
    including appending and prepending nodes, deleting nodes by value, searching for values,
    and displaying the list's contents.

    Attributes:
        head (Node): A reference to the head (first node) of the linked list.

    Methods:
        is_empty(): Check if the linked list is empty.
        append(data): Append a new node with the given data to the end of the linked list.
        prepend(data): Prepend a new node with the given data to the beginning of the linked list.
        delete(data): Delete the first occurrence of a node with the given data from the linked list.
        search(data): Search for a node with the given data in the linked list.
        display(): Display the contents of the linked list.
    """

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None

    def is_empty(self):
        """
        Check if the linked list is empty.

        Returns:
            bool: True if the linked list is empty, False otherwise.
        """
        return self.head is None

    def append(self, data):
        """
        Append a new node with the given data to the end of the linked list.

        Args:
            data: The data to be added to the linked list.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """
        Prepend a new node with the given data to the beginning of the linked list.

        Args:
            data: The data to be added to the linked list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def size(self):
        """Get the number of elements in the linked list.

        Returns:
            int: The number of elements in the linked list.
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def insert(self, data):
        """Insert a new element with the given data at the end of the list.

        Args:
            data: The data to be inserted.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def search(self, data):
        """Search for an element with the specified data in the list.

        Args:
            data: The data to search for.

        Returns:
            bool: True if the data is found, False otherwise.
        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete(self, data):
        """Delete the first occurrence of an element with the specified data.

        Args:
            data: The data to delete.
        """
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def get_list(self):
        """Get a list containing all elements in the linked list.

        Returns:
            list: A list of elements in the linked list.
        """
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def clear(self):
        """Clear the linked list by setting the head to None."""
        self.head = None

    def display(self):
        """
        Display the contents of the linked list.
        """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
