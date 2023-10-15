"""
Author: Rarghav Sharma(rghvsh)
trie.py - A Python implementation of a trie data structure.

This file contains the implementation of a trie data structure using a OOP and dictionary.
Tries also known as Prefix-Trees are a subcase of Trees which are used specially for storing
strings and makes the time complexity for searching a word O(n), where n is the length of the
word to be searched

The Trie class provides methods for adding words to the trie, checking whether a spcific
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
    """
        Represents a trie data structure implemented using a dictionary.
        
        A trie has a tree structure and stores string(s) by breaking them into charectars and storing them according 
        to their keys, here keys refers to the prefixes or the word which apear before any given charectar in the same 
        sequence as they appear in the word to be stored. Each charectar is connected to the one which appears before it in the word.
        
        Methods:
            
            insert(word): Inserts a word in the trie.
            search_word(sord): Searches for a word in the trie
            starts_with(substring): Searches for a substring in the begining of the words in the trie.
                 
     """

    def __init__(self):
        """
        Initialises  an empty dictionary and a variable to store Boolean values.
        """

      self.children = {}
      self.last_letter = False


    def insert(self, word):
        """
        Inserts a word in the trie data structure.

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
