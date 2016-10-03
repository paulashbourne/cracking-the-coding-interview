class TreeNode():

    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left  = left
        self.right = right

    def insert(self, node):
        if node.value <= self.value:
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        else:
            if self.right:
                self.right.insert(node)
            else:
                self.right = node

class BST():

    def __init__(self, root):
        self.root = root

    def insert(self, node):
        if self.root:
            self.root.insert(node)
        else:
            self.root = node
