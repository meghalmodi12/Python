"""
Given a binary tree, return its column order traversal from top to bottom and left to right Note: if two nodes are in the same row and column, order them from left to right

Ex: Given the following tree

    8
   / \
  2   29
     /  \
    3    9
return [[2], [8, 3], [29], [9]]
Ex: Given the following tree

     100
    /   \
  53     78
 / \    /  \
32  3  9    20
return [[32], [53], [100, 3, 9], [78], [20]]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def verticalTraversal(root):
    result = []
    
    if root is None:
        return result
    
    queue = deque()
    queue.append([root, 0])
    verticalLevelHashMap = {}
    minLevel, maxLevel = float('inf'), -float('inf')
    
    while queue:
        tempVerticalHashMap = {}
        
        for _ in range(len(queue)):
            node, vLevel = queue.popleft()
            minLevel = min(minLevel, vLevel)
            maxLevel = max(maxLevel, vLevel)

            if vLevel not in tempVerticalHashMap:
                tempVerticalHashMap[vLevel] = []
            tempVerticalHashMap[vLevel].append(node.val)

            if node.left:
                queue.append([node.left, vLevel - 1])

            if node.right:
                queue.append([node.right, vLevel + 1])
                
        for level, nodes in tempVerticalHashMap.items():
            if level not in verticalLevelHashMap:
                verticalLevelHashMap[level] = []
                
            verticalLevelHashMap[level].extend(sorted(nodes))
            
    for i in range(minLevel, maxLevel + 1):
        result.append(verticalLevelHashMap[i])
        
    return result
    