"""
Given a binary tree, returns of all its levels in a bottom-up fashion (i.e. last level towards the root). Ex: Given the following tree

        2
       / \
      1   2
return [[1, 2], [2]]
Ex: Given the following tree

       7
      / \
    6    2
   / \ 
  3   3 
return [[3, 3], [6, 2], [7]]
"""

from collections import deque

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def bottomsUp(root):
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

    return arrLevels[::-1]

# Test Case 1
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)

print(bottomsUp(root))


