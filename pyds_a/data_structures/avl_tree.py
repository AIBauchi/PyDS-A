"""Author: kaivalmehta
This code implements avl trees, and insertion , deletion in it. 
It also implements several traversals of the tree"""

class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = Node(9)

    def height(self, n):
        if n is None:
            return 0
        return n.height

    def _max(self, a, b):
        return a if a > b else b

    def balance(self, n):
        if n is None:
            return 0
        return self.height(n.left) - self.height(n.right)

    def left_rotate(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = 1 + self._max(self.height(x.left), self.height(x.right))
        y.height = 1 + self._max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        y.height = 1 + self._max(self.height(y.left), self.height(y.right))
        x.height = 1 + self._max(self.height(x.left), self.height(x.right))

        return x

    def insert(self, root, d):
        if root is None:
            return Node(d)

        if d > root.data:
            root.right = self.insert(root.right, d)
        else:
            root.left = self.insert(root.left, d)

        root.height = 1 + self._max(self.height(root.left), self.height(root.right))
        bf = self.balance(root)

        if bf > 1 and d < root.left.data:
            return self.right_rotate(root)
        if bf > 1 and d > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if bf < -1 and d > root.right.data:
            return self.left_rotate(root)
        if bf < -1 and d < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def find_min(self, root):
        tmp = root
        while tmp.left is not None:
            tmp = tmp.left
        return tmp

    def delete(self, root, val):
        if root is None:
            return root

        if val < root.data:
            root.left = self.delete(root.left, val)
        elif val > root.data:
            root.right = self.delete(root.right, val)
        else:
            if root.left is None and root.right is None:
                return None
            if root.left is None and root.right is not None:
                tmp = root.right
                root = None
                return tmp
            if root.left is not None and root.right is None:
                tmp = root.left
                root = None
                return tmp
            if root.left is not None and root.right is not None:
                minimum = self.find_min(root.right).data
                root.data = minimum
                root.right = self.delete(root.right, minimum)

        if root is None:
            return root

        root.height = 1 + self._max(self.height(root.right), self.height(root.left))
        bf = self.balance(root)

        if bf > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)
        if bf > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if bf < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)
        if bf < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return
        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=" ")

#Example Usage
avl_tree = AVL()
avl_tree.root = avl_tree.insert(avl_tree.root, 5)
avl_tree.root = avl_tree.insert(avl_tree.root, 10)
avl_tree.root = avl_tree.insert(avl_tree.root, 2)
avl_tree.root = avl_tree.insert(avl_tree.root, 12)
avl_tree.root = avl_tree.insert(avl_tree.root, 8)

print("Inorder Traversal:")
avl_tree.inorder(avl_tree.root)
print("\nPreorder Traversal:")
avl_tree.preorder(avl_tree.root)
print("\nPostorder Traversal:")
avl_tree.postorder(avl_tree.root)
