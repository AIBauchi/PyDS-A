# pyds_a/__init__.py

"""
PyDS-A: A Python Library for Data Structures and Algorithms

PyDS-A is a Python library that provides a collection of data structures and algorithms
to help you with various programming tasks.

Usage:
    - Import specific modules or classes from subpackages.
    - Access package-level variables and functions.

Example:
    To use the LinkedList class:
    >>> from pyds_a.data_structures.linked_list import LinkedList
    >>> linked_list = LinkedList()
    >>> linked_list.insert(42)
    >>> print(linked_list.size())

Package Contents:
    - data_structures: Subpackage containing various data structures.
    - algorithms: Subpackage containing algorithms.
    - PACKAGE_VERSION: The version of this PyDS-A package.
    - greet(): A function to provide a welcome message.

For more information and examples, visit the PyDS-A GitHub repository:
https://github.com/AIBauchi/PyDS-A
"""

# Import specific modules or classes from subpackages
from .data_structures.linked_list import LinkedList
from .algorithms.searching import binary_search
from .algorithms import *
from .data_structures import *

# Define package-level variables
PACKAGE_VERSION = "1.0.0"

# Define package-level function
def author():
    """Provide a welcome message for PyDS-A users.

    Returns:
        str: A welcome message.
    """
    return "Welcome to PyDS-A! an AIBauchi Initiative"
