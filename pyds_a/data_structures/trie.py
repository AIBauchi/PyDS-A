"""
Author: Rarghav Sharma(rghvsh)
trie.py - A Python implementation of a trie data structure.

This file contains the implementation of a trie data structure using a OOP.
A queue follows the First-In-First-Out (FIFO) principle, where the first element added
to the queue is the first one to be removed.

The trie class provides methods for adding words to the trie, checking whether a spcific
word is present in the trie, and to see whether the words in the trie start from a specific 
prefix/substring.

Usage:
    from trie import Trie

    i = Trie()
    i.insert("Apple")
    i.insert("Abacus")


    i.search_word("Apple") # True
    i.search_word("Adargrad") # False
    i.starts_with("Ac") # False
    i.starts_with("Aba") # True

"""


class Trie:

    def __init__(self):
        """
        Initialises trie data structure with an empty dictionary and a variable to store Boolean values.
        """
      self.children = {}
      self.last_letter = False


    def insert(self, word):
        """
        Inserts a word in the trie data structure

        Args :
            word (string): The word to be added                
        """
      root = self
      for char in word:
        if char not in root.children:
          root.children[char] = Trie()

        root = root.children[char]

      root.last_letter = True


    def search_word(self, word):
        """
        Searches for a word in the trie data structure.

        Args:
            word (string): The word which needs to be searched for in the trie.

        Returns:
            bool : Returns a boolean value whether the word is present in the trie.
        """
      root = self
      for char in word:
        if char not in root.children:
          return False

        else:
          root = root.children[char]
      return root.last_letter


    def starts_with(self, substring):
         """
        Searches whether there are words in the trie which start with the given substring.

        Args:
            substring (string): The prefix/substring with which word(s) in trie should start with.

        Returns:
            bool : Returns a boolean value whether there are words in the trie which begin with the given substring.
        """
      root = self
      for char in substring:
        if char not in root.children:
          return False

        else:
          root = root.children[char]
      return True
