class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
  if root is not None:
    minimumDepth = 1
    traverseArr = [root]

    while len(traverseArr) > 0:
      currLevelNodeCount = len(traverseArr)

      for _ in range(currLevelNodeCount):
        currNode = traverseArr.pop(0)

        if currNode.left is None and currNode.right is None:
          return minimumDepth
        if currNode.left:
          traverseArr.append(currNode.left)
        if currNode.right:
          traverseArr.append(currNode.right)

      minimumDepth += 1

  return -1


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()