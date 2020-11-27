"""
Given an n-ary tree, return its level order traversal.
Note: an n-ary tree is a tree in which each node has no more than N children.

Ex: Give the following n-ary tree…

    8
  / | \
 2  3  29
return [[8], [2, 3, 29]]
Ex: Given the following n-ary tree…

     2
   / | \
  1  6  9
 /   |   \
8    2    2
   / | \
 19 12 90
return [[2], [1, 6, 9], [8, 2, 2], [19, 12, 90]]
"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from collections import deque

def levelOrder(root: 'Node'):
    result = []
    
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)
    
    while queue:
        currLevelNodes = []
        
        for _ in range(len(queue)):
            node = queue.popleft()
            currLevelNodes.append(node.val)
            
            if node.children:
                for child in node.children:
                    queue.append(child)
                    
        result.append(currLevelNodes)
        
    return result
    