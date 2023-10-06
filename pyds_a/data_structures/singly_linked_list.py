"""
Author: Racso-3141

This module defines a singly linked list data structure with basic operations 
like adding nodes, removing nodes, searching for a specific value, and displaying the 
list's contents.
"""


class Node:
    """
    Represents a node in a singly linked list.

    Attributes:
        data: The data stored in the node.
        next: Reference to the next node in the singly linked list.
    """

    def __init__(self, data):
        """
        Initialize a new Node with the given data.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next = None


class SinglyLinkedList:
    """
    Represents a singly linked list data structure.

    The SinglyLinkedList class provides basic operations for working with a linked list,
    including appending and prepending nodes, deleting nodes by value, searching for
    values, and displaying the list's contents.

    Attributes:
        head (Node): A reference to the head (first node) of the singly linked list.
        tail (Node): A reference to the tail (last node) of the singly linked list.
        size (int) : Number of nodes in the singly linked list.

    Methods:
        is_empty(): Check whether the singly linked list is empty.
        append(data): Add a new node with the given data to the end.
        prepend(data): Add a new node with the given data to the start.
        find_first(data): Find the first node with the given data.
        find_all(data): Find all nodes containing the given data.
        delete_first(data): Delete the first node with the given data.
        delete_all(data): Delete all nodes with the given data.
        get_list(): Get a list of all nodes in order.
        clear(): Clear the singly linked list by setting the head to None, tail to None,
        size to 0.
        display(): Print all nodes in a string.

    """

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        """
        Check whether the singly linked list is empty.

        Returns:
            bool: True if the singly linked list is empty, False otherwise.

        >>> l = SinglyLinkedList()
        >>> l.is_empty()
        True
        >>> l.append(1)
        >>> l.is_empty()
        False
        """
        return self.size == 0

    def append(self, data):
        """
        Add a new node with the given data to the end.

        Args:
            data: The data of the new node.

        >>> l = SinglyLinkedList()
        >>> l.append(1)
        >>> l.head.data
        1
        >>> l.tail.data
        1
        >>> l.size
        1
        >>> l.get_list()
        [1]
        >>> l.append(2)
        >>> l.head.data
        1
        >>> l.tail.data
        2
        >>> l.size
        2
        >>> l.get_list()
        [1, 2]
        >>> l.append(3)
        >>> l.head.data
        1
        >>> l.tail.data
        3
        >>> l.size
        3
        >>> l.get_list()
        [1, 2, 3]
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, data):
        """
        Add a new node with the given data to the start.

        Args:
            data: The data of the new node.

        >>> l = SinglyLinkedList()
        >>> l.prepend(1)
        >>> l.head.data
        1
        >>> l.tail.data
        1
        >>> l.size
        1
        >>> l.get_list()
        [1]
        >>> l.prepend(2)
        >>> l.head.data
        2
        >>> l.tail.data
        1
        >>> l.size
        2
        >>> l.get_list()
        [2, 1]
        >>> l.prepend(3)
        >>> l.head.data
        3
        >>> l.tail.data
        1
        >>> l.size
        3
        >>> l.get_list()
        [3, 2, 1]
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def find_first(self, data):
        """
        Find the first node with the given data.

        Args:
            data: Data of the node to be found.

        Returns:
            The first node that contains the provided data else None.

        >>> l = SinglyLinkedList()
        >>> l.append(1)
        >>> l.append(2)
        >>> l.append(3)
        >>> node = l.find_first(2)
        >>> node.data
        2
        >>> print(l.find_first(4))
        None
        """
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def find_all(self, data):
        """
        Find all nodes containing the given data.

        Args:
            data: Data of nodes to be found.

        Returns:
            list: A list of nodes containing the provided data if found else
            an empty list.

        >>> l = SinglyLinkedList()
        >>> l.append(1)
        >>> l.append(2)
        >>> l.append(2)
        >>> l.append(3)
        >>> nodes = l.find_all(2)
        >>> [node.data for node in nodes]
        [2, 2]
        >>> l.find_all(4)
        []
        """
        nodes_data = []
        current = self.head
        while current:
            if current.data == data:
                nodes_data.append(current)
            current = current.next
        return nodes_data

    def delete_first(self, data):
        """
        Delete the first node with the given data.

        Args:
            data: Data of the node to be deleted.

        >>> l = SinglyLinkedList()
        >>> l.append(1)
        >>> l.append(2)
        >>> l.append(1)
        >>> l.delete_first(1)
        >>> l.head.data
        2
        >>> l.tail.data
        1
        >>> l.size
        2
        >>> l.get_list()
        [2, 1]
        >>> l.delete_first(1)
        >>> l.head.data
        2
        >>> l.tail.data
        2
        >>> l.size
        1
        >>> l.get_list()
        [2]
        >>> l.delete_first(3)
        >>> l.head.data
        2
        >>> l.tail.data
        2
        >>> l.size
        1
        >>> l.get_list()
        [2]
        >>> l.delete_first(2)
        >>> l.head is None
        True
        >>> l.tail is None
        True
        >>> l.size
        0
        >>> l.get_list()
        []
        """
        if self.is_empty():
            return

        dm = Node(None)
        dm.next = self.head
        prev = dm

        while prev.next:
            if prev.next.data == data:
                prev.next = prev.next.next
                self.size -= 1
                break
            prev = prev.next

        self.head = dm.next
        if self.size == 0:
            self.head = None
            self.tail = None
        elif not prev.next:
            self.tail = prev

    def delete_all(self, data):
        """
        Delete all nodes with the given data.

        Args:
            data: Data of nodes to be deleted.

        >>> l = SinglyLinkedList()
        >>> l.append(2)
        >>> l.append(2)
        >>> l.append(3)
        >>> l.append(2)
        >>> l.delete_all(2)
        >>> l.head.data
        3
        >>> l.tail.data
        3
        >>> l.size
        1
        >>> l.get_list()
        [3]
        >>> l.delete_all(3)
        >>> l.head is None
        True
        >>> l.tail is None
        True
        >>> l.size
        0
        >>> l.get_list()
        []
        """
        if self.is_empty():
            return

        dm = Node(None)
        dm.next = self.head
        prev = dm

        while prev.next:
            if prev.next.data == data:
                prev.next = prev.next.next
                self.size -= 1
                continue
            prev = prev.next

        self.head = dm.next
        if self.size == 0:
            self.head = None
            self.tail = None
        else:
            self.tail = prev

    def get_list(self):
        """
        Get a list of all nodes in order.

         Returns:
             A list of all nodes in the singly linked list.

         >>> l = SinglyLinkedList()
         >>> l.append(1)
         >>> l.append(2)
         >>> l.get_list()
         [1, 2]
        """
        list = []
        current = self.head
        while current:
            list.append(current.data)
            current = current.next
        return list

    def clear(self):
        """
        Clear the singly linked list by setting the head to None, tail to None,
        size to 0.

        >>> l = SinglyLinkedList()
        >>> l.append(1)
        >>> l.clear()
        >>> l.head is None
        True
        >>> l.tail is None
        True
        >>> l.size == 0
        True
        """
        self.head = None
        self.tail = None
        self.size = 0

    def display(self):
        """
        Print all nodes of the singly linked list in a string.

        >>> l = SinglyLinkedList()
        >>> l.display()
        None
        >>> l.append(1)
        >>> l.display()
        1 -> None
        >>> l.append(2)
        >>> l.display()
        1 -> 2 -> None
        """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
