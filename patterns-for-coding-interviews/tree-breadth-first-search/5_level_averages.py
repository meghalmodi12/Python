class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
  result = []
  if root is not None:
    traverseArr = [root]

    while len(traverseArr) > 0:
      currLevelSum = 0
      currLevelLength = len(traverseArr)

      for _ in range(currLevelLength):
        currNode = traverseArr.pop(0)
        currLevelSum += currNode.val

        if currNode.left:
          traverseArr.append(currNode.left)
        if currNode.right:
          traverseArr.append(currNode.right)

      result.append(currLevelSum / currLevelLength)

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_averages(root)))


main()