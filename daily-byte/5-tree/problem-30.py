"""
Given a binary search tree, rearrange the tree such that it forms a linked list where all its values are in ascending order.

Ex: Given the following tree...
        5
       / \
      1   6
return...

1
 \
  5
   \
    6
Ex: Given the following tree...

       5
      / \
    2    9
   / \ 
  1   3 
return...

1
 \
  2
   \
    3
     \
      5
       \
        9
Ex: Given the following tree...

5
 \
  6
return...

5
 \
  6
"""

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class LLNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def binaryTreeToSotedLinkedList(root):
    sortedList = []
    head, current = None, None

    def inorder(root):
        if root is None:
            return

        inorder(root.left)
        sortedList.append(root.val)
        inorder(root.right)

    inorder(root)

    for num in sortedList:
        if head is None:
            head = LLNode(num)
            current = head
        else:
            current.next = LLNode(num)
            current = current.next

    return head

# Test Case 1
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(6)

binaryTreeToSotedLinkedList(root)