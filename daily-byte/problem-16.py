"""
This question is asked by Facebook. Given a linked list and a value n, remove the nth to last node and return the resulting list.

Ex: Given the following linked lists...

1->2->3->null, n = 1, return 1->2->null
1->2->3->null, n = 2, return 1->3->null
1->2->3->null, n = 3, return 2->3->null
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

def removeNthFromLast(head, n):
    if head is None:
        return

    length = 0
    current = head
    while current:
        current = current.next
        length += 1

    target = length - n

    if target == 0:
        head = head.next
    else:
        previous, current = None, head

        while target != 0:
            previous = current
            current = current.next
            target -= 1

        previous.next = current.next

    return head

# Prepare list 1
arr1 = [3,2,1]
list1 = LinkedList()

for num in arr1:
    list1.insertAtHead(num)

result = removeNthFromLast(list1.head, 3)

# Print result
while result:
    print(result.val, end = '->')
    result = result.next



    

