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

    def delete(self, data):
        """
        Delete the first occurrence of a node with the given data from the linked list.

        Args:
            data: The data to be deleted from the linked list.
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

    def search(self, data):
        """
        Search for a node with the given data in the linked list.

        Args:
            data: The data to be searched for.

        Returns:
            bool: True if the data is found, False otherwise.
        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        """
        Display the contents of the linked list.
        """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
