"""
This question is asked by Amazon. Given a non-empty linked list, return the middle node of the list. If the linked list contains an even number of elements, return the node closer to the end.


1->2->3->null, return 2
1->2->3->4->null, return 3
1->null, return 1
"""

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

def findMiddleElement(head):
    if head is None:
        return head

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Prepare list 1
arr1 = [1]
list1 = LinkedList()

for num in arr1:
    list1.insertAtHead(num)

result = findMiddleElement(list1.head)

# Print result
print(result.val)