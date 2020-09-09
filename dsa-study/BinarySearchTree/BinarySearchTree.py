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
        self.preorder(root.left)
        self.preorder(root.right)
    
    #O(n)
    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)

    def levelOrder(self, root, level):
        if root is None:
            return 
        else:
            if level == 1:
                print(root.data)
            else:
                self.levelOrder(root.left, level - 1)
                self.levelOrder(root.right, level - 1)

    # ltr is a boolean flag for left to right
    def levelOrderZigZag(self, root, level, ltr):
        if root is None:
            return 
        else:
            if level == 1:
                print(root.data)
            else:
                if ltr:
                    self.levelOrderZigZag(root.left, level - 1, ltr)
                    self.levelOrderZigZag(root.right, level - 1, ltr)
                else:
                    self.levelOrderZigZag(root.right, level - 1, ltr)
                    self.levelOrderZigZag(root.left, level - 1, ltr)

    def getTreeHeight(self, root):
        if root is None:
            return 0
        else:
            lHeight = self.getTreeHeight(root.left)
            rHeight = self.getTreeHeight(root.right)

            if lHeight > rHeight:
                return lHeight + 1
            else:
                return rHeight + 1

    #O(1)
    def getRoot(self):
        return self.root

