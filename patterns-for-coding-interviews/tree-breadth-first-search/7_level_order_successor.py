from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
  if root:
    successorFound = False
    traverseArr = [root]
    while len(traverseArr) > 0:
      for _ in range(len(traverseArr)):
        currNode = traverseArr.pop(0)
        if successorFound:
          return currNode
        else:
          if currNode.val == key:
            successorFound = True
          
          if currNode.left:
            traverseArr.append(currNode.left)
          if currNode.right:
            traverseArr.append(currNode.right)

  return None


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  result = find_successor(root, 12)
  if result:
    print(result.val)
  result = find_successor(root, 9)
  if result:
    print(result.val)


main()
