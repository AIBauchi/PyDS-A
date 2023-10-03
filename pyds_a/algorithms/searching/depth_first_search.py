"""
depth_first_search.py: A python implementation of the Depth First Search (DFS) algorithm that is 
used to traverse and search graph data structures which is realised using an adjacency list. 
DFS generates nodes and compares them with the goal along the largest depth of the graph.
It uses a stack to realise the recursion in keeping track of visited nodes and unvisited neighbours. 

Author: davutgl

"""
from typing import List

def is_stack_empty(stack: List) -> bool:
    """
    Checks if the stack is empty.
    
    Args:
        stack (List): Stack to be checked.
        
    Returns:
        bool: True if the stack is empty, False otherwise.
    """
    return len(stack) == 0

def get_node_neighbours(node: str) -> List[str]:
    """
    Retrieves the neighbors of a given node in the graph.
    
    Args:
        node (str): Node for which neighbors are to be retrieved.
        
    Returns:
        List[str]: List of neighbouring nodes.
    """
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    # Checks if the node exists in the graph, if not, returns an empty list
    return graph.get(node, [])

def depth_first_search(starting_node: str, goal_node: str) -> bool:
    """
    Perform Depth-First Search on a graph to find the goal node.
    
    Args:
        starting_node (str): Node to start the search from.
        goal_node (str): Node to be searched.
        
    Returns:
        bool: True if the goal node is found, False otherwise.
    """
    stack = [starting_node]
    while not is_stack_empty(stack):
        stack_top_element = stack.pop()
        if stack_top_element == goal_node:
            return True  # Goal node is found
        else:
            # Add the neighbours of the current node to the stack
            neighbours = get_node_neighbours(stack_top_element)
            stack.extend(neighbours)
    return False  # Goal node is not found
