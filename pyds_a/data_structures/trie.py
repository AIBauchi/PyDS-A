"""
Author: Raghav Sharma(rghvsh)

Implements trie data structure and adds search
"""

class trie:

    def __init__(self):
      self.children = {}
      self.last_letter = False

    def insert(self, word):
      root = self
      for char in word:
        if char not in root.children:
          root.children[char] = trie()

        root = root.children[char]

      root.last_letter = True

    def search_word(self, word):
      root = self
      for char in word:
        if char not in root.children:
          return False

        else:
          root = root.children[char]
      return root.last_letter

    def starts_with(self, substring):
      root = self
      for char in substring:
        if char not in root.children:
          return False

        else:
          root = root.children[char]
      return True
