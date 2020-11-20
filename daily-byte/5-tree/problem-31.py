"""
Given a binary search tree that contains unique values and two nodes within the tree, a, and b, return their lowest common ancestor. Note: the lowest common ancestor of two nodes is the deepest node within the tree such that both nodes are descendants of it.

Ex: Given the following tree...
       7
      / \
    2    9
   / \ 
  1   5 
and a = 1, b = 9, return a reference to the node containing 7.
Ex: Given the following tree...

        8
       / \
      3   9
     / \ 
    2   6
and a = 2, b = 6, return a reference to the node containing 3.
Ex: Given the following tree...

        8
       / \
      6   9
and a = 6, b = 8, return a reference to the node containing 8.
"""

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

"""
- Maintain a hash map to track node - parent relationship
- Maintain until node1 and node2 are found
- Create a set containing path from node1 to root
- Start traversing from node2 to root and check if the node2's parent is found in the set
- When node2's parent is found in the set, break the loop and return ancestor's reference
"""
def lowestCommonAncestor(root, node1, node2):
    if root is None:
        return

    stack = [root]
    path = set()
    parentMap = {}
    parentMap[root] = None

    while node1 not in parentMap or node2 not in parentMap:
        node = stack.pop()

        if node.left:
            parentMap[node.left] = node
            stack.append(node.left)

        if node.right:
            parentMap[node.right] = node
            stack.append(node.right)

    while node1 is not None:
        path.add(node1)
        node1 = parentMap[node1]

    while node2 not in path:
        node2 = parentMap[node2]

    return node2

# Test Case 1
root = Node(7)
root.left = Node(2)
root.right = Node(9)
root.left.left = Node(1)
root.left.right = Node(5)

print(lowestCommonAncestor(root, root.left.left, root.right))

    