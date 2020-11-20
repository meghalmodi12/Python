"""
This question is asked by Google. Given a linked list and a value, remove all nodes containing the provided value, and return the resulting list.

Ex: Given the following linked lists and values...

1->2->3->null, value = 3, return 1->2->null
8->1->1->4->12->null, value = 1, return 8->4->12->null
7->12->2->9->null, value = 7, return 12->2->9->null
"""

from __future__ import print_function

# Node class
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtHead(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            node = Node(val)
            node.next = self.head
            self.head = node

def removeValue(head, value):
    if head is None:
        return

    # See if the value to be removed is at head position
    while head and head.val == value:
        head = head.next

    current = head
    while current and current.next:
        if current.next.val == value:
            current.next = current.next.next
        else:
            current = current.next

    return head

# Prepare list 1
arr1 = [1,3,2,1,1,4,1,1,1]
list1 = LinkedList()

for num in arr1:
    list1.insertAtHead(num)

result = removeValue(list1.head, 1)

# Print result
while result:
    print(result.val, end = '->')
    result = result.next

    

