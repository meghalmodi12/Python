"""
Given a binary search tree, return its mode (you may assume the answer is unique). If the tree is empty, return -1. Note: the mode is the most frequently occurring value in the tree.

Ex: Given the following tree...

        2
       / \
      1   2
return 2.

Ex: Given the following tree...

         7
        / \
      4     9
     / \   / \
    1   4 8   9
               \
                9  
return 9.
"""

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def findMode(root):
    if root is None:
        return root
    
    arrNode = []
    nodeDict = {}
    maxCount = 0
    result = []
    
    def inorder(root):
        if root is None:
            return 
        
        inorder(root.left)
        arrNode.append(root)
        inorder(root.right)
        
    inorder(root)
    
    for node in arrNode:
        if node.val not in nodeDict:
            nodeDict[node.val] = [node, 0]
        nodeDict[node.val][1] += 1
        
    for nodeVal, info in nodeDict.items():
        maxCount = max(maxCount, info[1])
        
    for nodeVal, info in nodeDict.items():
        if info[1] == maxCount:
            result.append(nodeVal)
    
    return result

# Test Case 1
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(2)

print(findMode(root))