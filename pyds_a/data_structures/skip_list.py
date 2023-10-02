"""
Author: Tinny-Robot

Based on "Skip Lists: A Probabilistic Alternative to Balanced Trees" by William Pugh
https://epaperpress.com/sortsearch/download/skiplist.pdf
"""

import random

class SkipListNode:
    """
    SkipListNode represents a node in the SkipList.

    Attributes:
        value: The value stored in the node.
        forward: A list of references to the forward nodes at different levels.
    """
    def __init__(self, value, level=0):
        """
        Initialize a SkipListNode.

        Args:
            value: The value to store in the node.
            level: The level of the node in the SkipList.
        """
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    """
    SkipList is a data structure for efficient search, insertion, and deletion in a sorted sequence.

    Attributes:
        head: The head node of the SkipList.
        level: The maximum level of the SkipList.
    """
    def __init__(self):
        """
        Initialize an empty SkipList.
        """
        self.head = SkipListNode(None, 0)
        self.level = 0

    def random_level(self):
        """
        Generate a random level for a new SkipListNode.

        Returns:
            int: The random level.
        """
        level = 0
        while random.random() < 0.5 and level < self.level + 1:
            level += 1
        return level

    def insert(self, value):
        """
        Insert a value into the SkipList.

        Args:
            value: The value to insert.
        """
        update = [None] * (self.level + 1)
        node = self.head

        for i in range(self.level, -1, -1):
            while node.forward[i] is not None and node.forward[i].value < value:
                node = node.forward[i]
            update[i] = node

        level = self.random_level()
        if level > self.level:
            for i in range(self.level + 1, level + 1):
                update.append(self.head)
            self.level = level

        new_node = SkipListNode(value, level)
        for i in range(level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def search(self, value):
        """
        Search for a value in the SkipList.

        Args:
            value: The value to search for.

        Returns:
            bool: True if the value is found, False otherwise.
        """
        node = self.head

        for i in range(self.level, -1, -1):
            while node.forward[i] is not None and node.forward[i].value < value:
                node = node.forward[i]

        if node.forward[0] is not None and node.forward[0].value == value:
            return True
        return False

    def delete(self, value):
        """
        Delete a value from the SkipList.

        Args:
            value: The value to delete.

        Returns:
            bool: True if the value is deleted, False if not found.
        """
        update = [None] * (self.level + 1)
        node = self.head

        for i in range(self.level, -1, -1):
            while node.forward[i] is not None and node.forward[i].value < value:
                node = node.forward[i]
            update[i] = node

        if node.forward[0] is not None and node.forward[0].value == value:
            for i in range(self.level + 1):
                if update[i].forward[i] != node.forward[i]:
                    break
                update[i].forward[i] = node.forward[i]

            while self.level > 0 and self.head.forward[self.level] is None:
                self.level -= 1

            return True
        return False

    def display(self):
        """
        Display the SkipList.
        """
        for level in range(self.level, -1, -1):
            node = self.head.forward[level]
            values = []
            while node is not None:
                values.append(node.value)
                node = node.forward[level]
            print(f"Level {level}: {values}")

# Example usage:
if __name__ == "__main__":
    skip_list = SkipList()
    elements = [3, 6, 9, 2, 7, 5, 8, 1, 4]

    for element in elements:
        skip_list.insert(element)

    skip_list.display()

    search_value = 7
    if skip_list.search(search_value):
        print(f"{search_value} found in the skip list.")
    else:
        print(f"{search_value} not found in the skip list.")

    delete_value = 5
    if skip_list.delete(delete_value):
        print(f"{delete_value} deleted from the skip list.")
    else:
        print(f"{delete_value} not found in the skip list.")

    skip_list.display()
