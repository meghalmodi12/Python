"""
Given a binary tree, return the largest value in each of its levels. Ex: Given the following tree

    2
   / \
  10  15
        \
         20
return [2, 15, 20]
Ex: Given the following tree

          1
         / \
        5   6
       / \   \  
      5   3   7 
return [1, 6, 7]
"""

from collections import deque

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def gatherMaxVals(root):
    result = []

    if root is None:
        return arrLevels

    queue = deque()
    queue.append(root)

    while queue:
        maxVal = -float('inf')

        for _ in range(len(queue)):
            node = queue.popleft()
            maxVal = max(maxVal, node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(maxVal)

    return result

# Test Case 1
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)

print(gatherMaxVals(root))

