class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def getHeight(root):
    if root is None:
        return 0

    leftHeight = getHeight(root.left)
    rightHeight = getHeight(root.right)

    return 1 + max(leftHeight, rightHeight)

def traverseLevel(node, level, arrNode, flag = False):
    if node is None:
        return arrNode

    if level == 1:
        if flag:
            arrNode.append(node.val)
        else:
            arrNode.insert(0, node.val)

    traverseLevel(node.left, level - 1, arrNode)
    traverseLevel(node.right, level - 1, arrNode)

def traverse(root):
    flag = True
    result = []
    treeHeight = getHeight(root)

    for h in range(1, treeHeight + 1):
        currLevelNodes = []
        traverseLevel(root, h, currLevelNodes, flag)
        result.append(currLevelNodes)
        flag = not flag

    return result

if __name__ == "__main__":
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order zig-zag traversal: " + str(traverse(root)))

