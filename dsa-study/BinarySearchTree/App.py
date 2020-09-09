from BinarySearchTree import BinarySearchTree
from Node import Node

binarySearchTree = BinarySearchTree()

binarySearchTree.insert(binarySearchTree.getRoot(), Node(50))
binarySearchTree.insert(binarySearchTree.getRoot(), Node(30))
binarySearchTree.insert(binarySearchTree.getRoot(), Node(20))
binarySearchTree.insert(binarySearchTree.getRoot(), Node(40))
binarySearchTree.insert(binarySearchTree.getRoot(), Node(70))
binarySearchTree.insert(binarySearchTree.getRoot(), Node(60))
binarySearchTree.insert(binarySearchTree.getRoot(), Node(80))

# Tree Height
print("Height : " , binarySearchTree.getTreeHeight(binarySearchTree.getRoot()))

# Inorder Traversal
print("Inorder Traversal")
binarySearchTree.inorder(binarySearchTree.getRoot())

# Level Order Traversal
print("Level Order Traversal")
treeHeight = binarySearchTree.getTreeHeight(binarySearchTree.getRoot())
for i in range(1, treeHeight + 1):
    binarySearchTree.levelOrder(binarySearchTree.getRoot(), i)

# Level Order Zig-Zag
print("Level Order Traversal Zig-Zag")
leftToRight = True
for i in range(1, treeHeight + 1):
    binarySearchTree.levelOrderZigZag(binarySearchTree.getRoot(), i, leftToRight)
    leftToRight = not leftToRight