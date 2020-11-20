"""
Given a binary search tree, return the minimum difference between any two nodes in the tree.

Ex: Given the following tree...
        2
       / \
      3   1
return 1.
Ex: Given the following tree...
        29
       /  \
     17   50
    /     / \
   1    42  59
return 8.
Ex: Given the following tree...
        2
         \
         100
return 98.
"""

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def getMinimumDifference(root):
    arrNums = []
    minDiff = float('inf')
    
    def inorder(root):
        if root is None:
            return 
        
        inorder(root.left)
        arrNums.append(root.val)
        inorder(root.right)
        
    inorder(root)

    for i in range(1, len(arrNums)):
        minDiff = min(minDiff, arrNums[i] - arrNums[i - 1])
        
    return minDiff

# Test Case 1
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(getMinimumDifference(root))