from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
    
    def getHead(self):
        return self.head

    def isEmpty(self):
        return self.head == None

    def insertAtHead(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        return self.head

    def insertAtTail(self, value):
        newNode = Node(value)
        if self.tail is None:
            self.head = newNode
        else:
            start = self.head
            while start.next:
                start = start.next
            start.next = newNode
        return self.head

    def getLength(self):
        if self.head is None:
            return 0
        
        count = 0
        start = self.head
        while start:
            count += 1
            start = start.next
        return count

    def convertToList(self):
        elements = []
        start = self.head
        while start:
            elements.append(str(start.value))
            start = start.next
        return elements

    def printList(self):
        elements = []
        start = self.head
        while start:
            elements.append(str(start.value))
            start = start.next
        elements.append('None')
        return "->".join(elements)
    