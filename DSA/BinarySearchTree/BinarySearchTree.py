class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    #O(log n)
    def insert(self, root, node):
        if root is None:
            self.root = node
        else:
            if root.data > node.data:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left, node)
            else:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right, node)

    def delete(self, root, key):
        if root is None:
            return root

    # Get minimum value node from BST
    def minValueNode(self, root):
        if root is not None:
            currNode = root
            while currNode.left is not None:
                currNode = currNode.left
            return currNode

    # Get maximum value node from BST
    def maxValueNode(self, root):
        if root is not None:
            currNode = root
            while currNode is not None:
                currNode = currNode.right
            return currNode

    #O(n)
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

    #O(n)
    def preorder(self, root):
        if root is None:
            return
        print(root.data)
        self.inorder(root.left)
        self.inorder(root.right)
    
    #O(n)
    def postorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.inorder(root.right)
        print(root.data)

    #O(1)
    def getRoot(self):
        return self.root

