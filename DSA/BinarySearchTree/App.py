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

binarySearchTree.inorder(binarySearchTree.getRoot())