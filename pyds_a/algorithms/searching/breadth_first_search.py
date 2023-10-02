"""
Author: Racso-3141


breadth_first_search.py - A Python implementation of the Breadth First
Search algorithm.


This script offers a pure Python implementation of the Breadth First
Search(BFS) algorithm. BFS is used for traversing or searching a graph
in level order. Specifically, the BFS algorithm ensures that all nodes
at the current depth are processed before moving to nodes at the next
depth level. A queue is employed as the primary data structure to
achieve this systematic traversal.


For doctests run the following command: python3 -m doctest -v
breadth_first_search.py


For manual testing run: python3 fibonacci_search.py
"""


from collections import deque


def breadth_first_search(graph: dict, start: int) -> list:
    """
    Implements the Breadth First Search (BFS) algorithm to traverse
    or search through a graph.


    Args:
    - graph (dict): The graph, represented as an adjacency list where keys are
    integers and values are lists of integers.
    - start (int): The starting node for the BFS traversal.


    Returns:
    - list: A list of nodes, representing the order of traversal by BFS.


    Examples:
    # Argument checks:
    >>> breadth_first_search(None, 1)
    Traceback (most recent call last):
    ...
    ValueError: The 'graph' argument must not be None.


    >>> breadth_first_search([], 1)
    Traceback (most recent call last):
    ...
    TypeError: Expected 'graph' type 'dict', but got 'list'


    >>> breadth_first_search({}, 1)
    Traceback (most recent call last):
    ...
    ValueError: The 'graph' argument must not be empty.


    >>> graph = {1: [2, 3], 2: [4, 5], 3: [], 4: [], 5: []}
    >>> breadth_first_search(graph, '1')
    Traceback (most recent call last):
    ...
    TypeError: Expected 'start' type 'int', but got 'str'


    >>> breadth_first_search(graph, 7)
    Traceback (most recent call last):
    ...
    ValueError: The 'graph' does not contain 'start': 7.


    # BFS functionality:
    >>> breadth_first_search(graph, 1)
    [1, 2, 3, 4, 5]


    >>> graph2 = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
    >>> breadth_first_search(graph2, 1)
    [1, 2, 3]


    # Graph with loops:
    >>> graph3 = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2], 4: [2]}
    >>> breadth_first_search(graph3, 1)
    [1, 2, 3, 4]


    # Graph with isolated nodes:
    >>> graph4 = {1: [2], 2: [1], 3: [], 4: []}
    >>> breadth_first_search(graph4, 1)
    [1, 2]
    """

    if graph is None:
        raise ValueError("The 'graph' argument must not be None.")
    if not isinstance(graph, dict):
        raise TypeError(
            f"Expected 'graph' type 'dict', but got '{type(graph).__name__}'"
        )
    if not graph:
        raise ValueError("The 'graph' argument must not be empty.")
    if not isinstance(start, int):
        raise TypeError(
            f"Expected 'start' type 'int', but got '{type(start).__name__}'"
        )
    if start not in graph:
        raise ValueError(f"The 'graph' does not contain 'start': {start}.")

    visited = set()
    visited.add(start)
    queue: deque[int] = deque()
    queue.append(start)

    bfs_result = []
    while len(queue):
        for _ in range(len(queue)):
            node = queue.popleft()
            bfs_result.append(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    return bfs_result
