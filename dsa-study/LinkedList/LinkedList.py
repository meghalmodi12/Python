from Node import Node

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.count = 0

    # O(1)
    def insertAtStart(self, data):
        newNode = Node(data)
        self.count += 1
        if self.head is None:
            self.head = newNode 
        else:
            newNode.nextNode = self.head
            self.head = newNode

    #O(n)
    def insertAtEnd(self, data):
        currentNode = self.head
        newNode = Node(data)
        self.count += 1

        while currentNode.nextNode is not None:
            currentNode = currentNode.nextNode

        currentNode = newNode

    #O(n)
    def remove(self, data):
        if self.head:

            if self.head.data == data:
                self.head = self.head.nextNode
                return
            
            previousNode = self.head
            currentNode = self.head.nextNode

            while currentNode is not None:
                if currentNode.data == data:
                    break
                else:
                    previousNode = previousNode.nextNode
                    currentNode = currentNode.nextNode

            if currentNode is None:
                return

            previousNode.nextNode = currentNode.nextNode
            currentNode = None

    def traverse(self):
        currentNode = self.head

        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.nextNode

    #O(1)
    def size(self):
        return self.count