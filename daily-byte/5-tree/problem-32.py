"""
Given an array of numbers sorted in ascending order, return a height balanced binary search tree using every number from the array. Note: height balanced meaning that the level of any node’s two subtrees should not differ by more than one.

Ex: nums = [1, 2, 3] return a reference to the following tree...
       2
      /  \
     1    3
Ex: nums = [1, 2, 3, 4, 5, 6] return a reference to the following tree...
        3
       / \
     2    5
    /   /  \
  1    4    6
"""

# Recursive approach
class RTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class RSolution:
    def solve(self, nums):
        if len(nums) == 0:
            return
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.solve(nums[:mid])
        root.right = self.solve(nums[mid + 1:])
        
        return root

        