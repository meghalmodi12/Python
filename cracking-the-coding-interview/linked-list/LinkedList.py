class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = new_node

    def generate(self, items):
        for item in items:
            self.insert(item)

    def printList(self):
        result = []
        curr_node = self.head
        
        while curr_node is not None:
            result.append(str(curr_node.data))
            curr_node = curr_node.next
        result.append('None')

        print(" -> ".join(result)) 

