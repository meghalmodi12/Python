"""
Given a binary tree return all the values you’d be able to see if you were standing on the left side of it with values ordered from top to bottom.

Ex: Given the following tree

-->    4
      / \
-->  2   7
return [4, 2]
Ex: Given the following tree

-->        7
         /  \
-->     4     9
       / \   / \
-->   1   4 8   9
                 \
-->               9
return [7, 4, 1, 9]
"""

from collections import deque

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def visibleValues(root):
    result = []

    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        for i in range(len(queue)):
            node = queue.popleft()

            if i == 0:
                result.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return result

# Test Case 1
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)

print(visibleValues(root))
