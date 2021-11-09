class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    """
    The insert method supports duplicate values, it will always be inserted to the right

    Time : Average O(log(n)) | Worst O(n)
    Space : O(1)
    """
    def insert(self, value):
        currentNode = self

        while True:
            if currentNode.value > value:
                if not currentNode.left:
                    currentNode.left = BinarySearchTree(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if not currentNode.right:
                    currentNode.right = BinarySearchTree(value)
                else:
                    currentNode = currentNode.right

        return self

    """
    Time : Average O(log(n)) | Worst O(n)
    Space : O(1)
    """
    def contains(self, value):
        currentNode = self

        while currentNode:
            if currentNode.value > value:
                currentNode = currentNode.left
            elif currentNode.value < value:
                currentNode = currentNode.right
            else:
                return True

        return False

    """
    Time : Average O(log(n)) | Worst O(n)
    Space : O(1)
    """
    def remove(self, value, parentNode = None):
        currentNode = self
        parentNode = None

        while currentNode:
            if currentNode.value > value:
                currentNode = currentNode.left
            elif currentNode.value < value:
                currentNode = currentNode.right
            else:
                """
                Case 1 :  Both left and right child exist
                - In this case find the minimum value from the right subtree 
                - Update the value of the current node
                - Remove the node with minimum value from the right subtree
                - Key is to call remove method on the right subtree of the current node and not on root
                """ 
                if currentNode.left and currentNode.right:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                """
                Case 2 : When the current node is root (When parent node is none) 
                and left / right / left and right subtree is not available 
                """
                elif parentNode is None:
                    """
                    Case 2.1 : When the right subtree is not available
                    - Set current node value to current node's left node value
                    - Set current node right -> current node left - right
                    - Set current node left -> current node left - left
                    """
                    if currentNode.left:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    """
                    Case 2.2 : When the left subtree is not available
                    - Set current node value to current node's left node value
                    - Set current node right -> current node left - right
                    - Set current node left -> current node left - left
                    """
                    elif currentNode.right:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    """
                    Case 2.3 : When left and right subtree is not available
                    """
                    else:
                        pass
                """
                Case 3 : When current node does not have both the children
                and current node is not the root node 
                and parent node's left is current node
                """
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left else currentNode.right
                """
                Case 4 : When current node does not have both the children
                and current node is not the root node 
                and parent node's right is current node
                """
                elif parentNode.right == currentNode
                    parentNode.right = currentNode.left if currentNode.left else currentNode.right
                else:
                    pass
            break

        return self

    """
    Time : Average O(log(n)) | Worst O(n)
    Space : O(1)
    """
    def getMinValue(self):
        currentNode = self

        while currentNode.left:
            currentNode = currentNode.left
        
        return currentNode.value


