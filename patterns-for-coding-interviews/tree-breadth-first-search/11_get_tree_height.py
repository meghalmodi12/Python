class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def get_tree_height(root):
  if root is None:
    return 0

  height = 0
  queue = [root]

  while True:
    nodeCount = len(queue)
    if nodeCount == 0:
      return height

    height += 1
    for _ in range(nodeCount):
      node = queue.pop(0)
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.left.left.left = TreeNode(3)
  print("Height of the tree : " + str(get_tree_height(root)))

main()