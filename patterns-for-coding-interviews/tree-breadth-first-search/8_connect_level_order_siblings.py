from __future__ import print_function


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # level order traversal using 'next' pointer
  def print_level_order(self):
    nextLevelRoot = self
    while nextLevelRoot:
      current = nextLevelRoot
      nextLevelRoot = None
      while current:
        print(str(current.val) + " ", end='')
        if not nextLevelRoot:
          if current.left:
            nextLevelRoot = current.left
          elif current.right:
            nextLevelRoot = current.right
        current = current.next
      print()


def connect_level_order_siblings(root):
  if root:
    prevNode = None
    traverseArr = [root]

    while len(traverseArr) > 0:
      prevNode = None
      currLevelLength = len(traverseArr)

      for i in range(currLevelLength):
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
  connect_level_order_siblings(root)

  print("Level order traversal using 'next' pointer: ")
  root.print_level_order()


main()