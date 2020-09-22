class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_sum_of_path_numbers(root):
  result = 0
  stack = [root]
  parent = { root: [[root.val], False] }

  while stack:
    node = stack.pop()

    if node.left:
      stack.append(node.left)
      pathFromRoot = parent[node][0][:]
      pathFromRoot.append(node.left.val)
      parent[node.left] = [pathFromRoot, False]

    if node.right:
      stack.append(node.right)
      pathFromRoot = parent[node][0][:]
      pathFromRoot.append(node.right.val)
      parent[node.right] = [pathFromRoot, False]

    if not node.left and not node.right:
      parent[node][1] = True

  for info in parent.values():
    if info[1] == True:
        result += convert_to_number(info[0][::-1])

  return result

def convert_to_number(nums):
  result = 0
  mulitplier = 1

  for num in nums:
    result += mulitplier * num
    mulitplier *= 10

  return result

def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
