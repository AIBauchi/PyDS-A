"""Author: Rarghav Sharma(rghvsh)
tree.py - A Python implementation of a tree data structure.

This file contains the implementation of a tree data structure using a OOP and list.
Trees are a non linear data structure in which the members are connected using references
in a heirarchical manner in the form of parent and child node, where a child node can be a parent node for other nodes.

The Tree class provides methods for adding child nodes(data) to the tree, checking how deep a node is in
the tree, and to print the entire tree structure in a heirarchichal manner such  that the heirarchy is visible.

Usage:
    from tree import Tree
    laptop = Tree("Laptop")
    laptop.add_child("Acer")

    laptop.add_child("Apple")
    laptop.add_child("Asus")

    mobile = Tree("Mobile")

    mobile.add_child("Apple")
    mobile.add_child("Tecno")

    electronics = Tree("Electronics")
    electronics.add_child(laptop)
    electronics.add_child(mobile)

    print(mobile.levels()) #Returns 1

    electronics.print_tree()

    the above program Prints this:
      Electronics
        Laptop
            Acer
            Apple
            Asus
        Mobile
            Apple
            Tecno

"""

class Tree:
  """
        Represents a tree data structure implemented using a list.

        A tree is a non linear data structure in which the members are connected using references in a heirarchical manner
        in the form of parent and child node, where a child node  can be a parent node for other nodes.

        Methods:
            add_child(word): Inserts a child node in the tree.
            levels(): Shows the number of layers above the given node.
            print_tree(): Prints the entire tree. With all child nodes.

  """

  def __init__(self, data):
    """
        Initialises an empty tree via list.
    """
    self.data = data
    self.children = []
    self.parent = None


  def add_child(self, child):
    """
        Adds a node to the tree .

        Args:
            child (any) : Takes input in any format converts it into a tree node if not already and adds it to the tree.
    """
    if type(child) ==  Tree:
      child_node = child
      self.children.append(child)
      child_node.data = child.data
      child_node.parent = self

    else:
      child_node = Tree(child)
      child_node.parent = self
      child_node.data = child
      self.children.append(child_node)


  def levels(self):
    """
        Returns the level/how deep a node is in the tree i.e. how many layers above it.

        Returns:
            int : Returns an integer value the number of layers above the given node in the tree.
    """

    level = 0
    x = self.parent

    while x:
      level=level+1
      x = x.parent

    return level


  def print_tree(self):
    """
        Prints the structure of the tree.
   """
    x = self.levels()
    spaces = " " * int(x) *3
    print(spaces + self.data)

    if len(self.children) > 0 :
      for child in self.children:
        child.print_tree()
