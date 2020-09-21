class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def has_path(root, sum):
  if root is None:
    return

  stack = [root]
  parent = {root: [root.val, False]}

  while stack:
    node = stack.pop()
    if node.left:
      stack.append(node.left)
      parent[node.left] = [parent[node][0] + node.left.val, False]

    if node.right:
      stack.append(node.right)
      parent[node.right] = [parent[node][0] + node.right.val, False]

    if not node.left and not node.right:
        parent[node][1] = True

  for node, info in parent.items():
    if info[0] == sum and info[1] == True:
        return True

  return False

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has path: " + str(has_path(root, 23)))
  print("Tree has path: " + str(has_path(root, 16)))


main()
