class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
  allPaths = []
  stack = [root]
  parent = { root: [str(root.val), False] }

  strSeq = "".join([str(s) for s in sequence])

  while stack:
    node = stack.pop()
    if node.left:
      stack.append(node.left)
      pathToRoot = parent[node][0] + str(node.left.val)
      parent[node.left] = [pathToRoot, False]
    if node.right:
      stack.append(node.right)
      pathToRoot = parent[node][0] + str(node.right.val)
      parent[node.right] = [pathToRoot, False]
    if not node.left and not node.right:
      if parent[node][0] == strSeq:
        return True

  return False

def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
