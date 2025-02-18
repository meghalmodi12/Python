from __future__ import print_function

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next


def connect_all_siblings(root):
  if root:
    prevNode = None
    traverseArr = [root]

    while len(traverseArr) > 0:
      for _ in range(len(traverseArr)):
        currNode = traverseArr.pop(0)
        if prevNode:
          prevNode.next = currNode
        prevNode = currNode

        if currNode.left:
          traverseArr.append(currNode.left)
        if currNode.right:
          traverseArr.append(currNode.right)

    currNode.next = None

  return


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_all_siblings(root)
  root.print_tree()


main()
