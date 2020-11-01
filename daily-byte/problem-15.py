"""
This question is asked by Apple. Given two sorted linked lists, merge them together in ascending order and return a reference to the merged list

Ex: Given the following lists...

list1 = 1->2->3, list2 = 4->5->6->null, return 1->2->3->4->5->6->null
list1 = 1->3->5, list2 = 2->4->6->null, return 1->2->3->4->5->6->null
list1 = 4->4->7, list2 = 1->5->6->null, return 1->4->4->5->6->7->null
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

def mergeLinkedList(l1, l2):
    head, current = None, None

    while l1 or l2:
        node = None
        if l1 and l2:
            if l1.val < l2.val:
                node = Node(l1.val)
                l1 = l1.next
            else:
                node = Node(l2.val)
                l2 = l2.next
        elif l2:
            node = Node(l2.val)
            l2 = l2.next
        else:
            node = Node(l1.val)
            l1 = l1.next

        if head is None:
            head = node
            current = head
        else:
            current.next = node
            current = current.next

    return head

# Prepare list 1
arr1 = [9,7,5,3,1]
list1 = LinkedList()

for num in arr1:
    list1.insertAtHead(num)

# Prepare list 2
arr2 = [8,6,4,2]
list2 = LinkedList()

for num in arr2:
    list2.insertAtHead(num)

# Generate merged list
result = mergeLinkedList(list1.head, list2.head)

# Print result
while result:
    print(result.val, end = '->')
    result = result.next



