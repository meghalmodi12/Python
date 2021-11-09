from Tree import BinarySearchTree_Old

# DFS with a small change - Add right to stack and then add left to stack
def preOrderTraversal(root):
    if root is None:
        return None

    result = []
    stack = [root]

    while stack:
        currNode = stack.pop()
        result.append(currNode.value)

        if currNode.right:
            stack.append(currNode.right)

        if currNode.left:
            stack.append(currNode.left)

    return result

BST = BinarySearchTree_Old(6)
BST.insert(4)
BST.insert(9)
BST.insert(5)
BST.insert(2)
BST.insert(8)
BST.insert(12)

result = preOrderTraversal(BST.root)

print(result)