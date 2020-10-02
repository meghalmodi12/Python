from Node import Node

class BinarySearchTree:
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.insert(value)

    def search(self, value):
        if self.root is None:
            print('Tree is empty!')
        else:
            searchResult = self.root.search(value)
            if searchResult is False:
                print(str(value) + ' not found in the tree')

    def delete(self, value):
        if self.root is None:
            print('Tree is empty!')
        else:
            self.root = self.root.delete(value)