class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currNode = self
        parent = None

        while currNode:
            parent = currNode
            if value < currNode.value:
                currNode = currNode.left
            else:
                currNode = currNode.right

        if value < parent.value:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

        return True

    def search(self, value):
        currNode = self
        nodeFound = False

        while currNode and not nodeFound:
            if value == currNode.value:
                nodeFound = True
            elif value < currNode.value:
                currNode = currNode.left
            else:
                currNode = currNode.right

        return currNode if nodeFound else False

    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
            else:
                return None
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
            else:
                return None
        else:
            # Node to be deleted is leaf node
            if self.left is None and self.right is None:
                self = None
                return None
            # Node to be deleted has single child (left)
            elif self.right is None:
                tempNode = self.left
                self = None
                return tempNode
            # Node to be deleted has single child (right)
            elif self.left is None:
                tempNode = self.right
                self = None
                return tempNode
            # Node to be deleted has both left and right child
            else:
                currNode = self.right
                while currNode.left:
                    currNode = currNode.left
                self.value = currNode.value
                self.right = self.right.delete(currNode.value)

        return self

