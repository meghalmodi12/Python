from Node import Node

class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, data):
        newNode = Node(data)
        return newNode