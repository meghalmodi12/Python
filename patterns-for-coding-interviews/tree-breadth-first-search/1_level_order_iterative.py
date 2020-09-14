class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root, reverse = False):
  result = []
  
  if root is None:
    return result

  traverseArr = [root]
  while len(traverseArr) > 0:
    currLevelSize = len(traverseArr)
    currLevel = []

    for _ in range(currLevelSize):
      currNode = traverseArr.pop(0)
      currLevel.append(currNode.val)
      if currNode.left:
        traverseArr.append(currNode.left)
      if currNode.right:
        traverseArr.append(currNode.right)

    result.append(currLevel)

  if reverse:
    return result[::-1]
  return result

if __name__ == "__main__":
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverseZigZag(root)))
