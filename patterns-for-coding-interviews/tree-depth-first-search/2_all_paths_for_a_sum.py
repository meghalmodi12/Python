class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root, sum):
  allPaths = []
  
  stack = [root]
  parent = {root: [[root.val], root.val, False]}

  while stack:
      node = stack.pop()

      if node.left:
          stack.append(node.left)
          pathFromRoot = parent[node][0][:]
          pathFromRoot.append(node.left.val)
          parent[node.left] = [pathFromRoot, parent[node][1] + node.left.val, False]

      if node.right:
          stack.append(node.right)
          pathFromRoot = parent[node][0][:]
          pathFromRoot.append(node.right.val)
          parent[node.right] = [pathFromRoot, parent[node][1] + node.right.val, False]

      if not node.left and not node.right:
          parent[node][2] = True

  for node, info in parent.items():
      if info[1] == sum and info[2] == True:
          allPaths.append(info[0])

  return allPaths


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sum = 23
  print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))

main()
