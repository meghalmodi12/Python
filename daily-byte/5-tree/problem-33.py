"""
Given two binary trees, return whether or not the two trees are identical. Note: identical meaning they exhibit the same structure and the same values at each node. Ex: Given the following trees...

        2
       / \
      1   3
    2
   / \
  1   3

return true.

Ex: Given the following trees...

        1
         \
          9
           \
           18
    1
   /
  9
   \
    18

return false.

Ex: Given the following trees...

        2
       / \
      3   1
    2
   / \
  1   3

return false.   
"""

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    if not p and not q:
        return True

    if not p or not q:
        return False

    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# Test Case 1
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(4)

print(isSameTree(root1, root2))