from __future__ import print_function

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def tree_side_view(root, view = 'right'):
  result = []
  
  if root:
    traverseArr = [root]

    while len(traverseArr) > 0:
      currLevelLength = len(traverseArr)
      for i in range(currLevelLength):
        currNode = traverseArr.pop(0)

        if view == 'right':
          if i == currLevelLength - 1:
            result.append(currNode)
        if view == 'left':
          if i == 0:
            result.append(currNode)

        if currNode.left:
          traverseArr.append(currNode.left)
        if currNode.right:
          traverseArr.append(currNode.right)

  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.left.left.left = TreeNode(3)
  result = tree_side_view(root, 'right')
  print("Tree side view: ")
  for node in result:
    print(str(node.val) + " ", end='')


main()