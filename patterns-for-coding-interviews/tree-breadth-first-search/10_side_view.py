from __future__ import print_function

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def tree_side_view(root, view = 'right'):
  result = []
  
  if root:
    levelOrderTraverse = []
    traverseArr = [root]

    while len(traverseArr) > 0:
      currLevelNodes = []

      for _ in range(len(traverseArr)):
        currNode = traverseArr.pop(0)
        currLevelNodes.append(currNode)

        if currNode.right:
          traverseArr.append(currNode.right)
        if currNode.left:
          traverseArr.append(currNode.left)
        
      levelOrderTraverse.append(currLevelNodes)

    for level in levelOrderTraverse:
      if view == 'left':
        result.append(level[-1])
      else:
        result.append(level[0])

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