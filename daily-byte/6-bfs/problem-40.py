"""
Given a binary tree, return its zig-zag level order traversal (i.e. its level order traversal from left to right the first level, right to left the level the second, etc.).

Ex: Given the following tree

    1
   / \
  2   3
return [[1], [3, 2]]
Ex: Given the following tree

    8
   / \
  2  29
    /  \
   3    9
return [[8], [29, 2], [3, 9]]
"""

from collections import deque

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def traverseZigZag(root):
    result = []

    if root is None:
        return result

    level = 0
    queue = deque()
    queue.append(root)

    while queue:
        currLevelNodes = []

        for _ in range(len(queue)):
            node = queue.popleft()
            currLevelNodes.append(node.val)

            if level % 2 == 0:
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            else:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        level += 1
        result.append(currLevelNodes)

    return result

# Test Case 1
root = TreeNode(8)
root.left = TreeNode(2)
root.right = TreeNode(29)
root.right.left = TreeNode(3)
root.right.right = TreeNode(9)

print(traverseZigZag(root))