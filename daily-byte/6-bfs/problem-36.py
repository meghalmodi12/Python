"""
Given a binary tree, return its level order traversal where the nodes in each level are ordered from left to right.

Ex: Given the following tree...

    4
   / \
  2   7
return [[4], [2, 7]]
Ex: Given the following tree...

    2
   / \
  10  15
        \
         20
return [[2], [10, 15], [20]]
Ex: Given the following tree...

    1
   / \
  9   32
 /      \
3        78
return [[1], [9, 32], [3, 78]]
"""

from collections import deque

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def gatherLevels(root):
    arrLevels = []

    if root is None:
        return arrLevels

    queue = deque()
    queue.append(root)

    while queue:
        currLevel = []

        for _ in range(len(queue)):
            node = queue.popleft()
            currLevel.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        arrLevels.append(currLevel)

    return arrLevels

# Test Case 1
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)

print(gatherLevels(root))


