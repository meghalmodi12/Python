class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def count_paths(root, S):
  result = 0
  stack = [root]
  parent = { root: [root.val] }

  while stack:
    node = stack.pop()

    if node.left:
      stack.append(node.left)
      pathFromRoot = parent[node][:]
      pathFromRoot.append(node.left.val)
      parent[node.left] = pathFromRoot

    if node.right:
      stack.append(node.right)
      pathFromRoot = parent[node][:]
      pathFromRoot.append(node.right.val)
      parent[node.right] = pathFromRoot

  for path in parent.values():
    if get_target_sum(path, S):
      result += 1

  return result

def get_target_sum(nums, target):
  tempSum, windowStart = 0, 0

  for windowEnd in range(len(nums)):
    tempSum += nums[windowEnd]

    while tempSum > target:
      tempSum -= nums[windowStart]
      windowStart += 1

    if tempSum == target:
      return True

  return False

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))

main()
