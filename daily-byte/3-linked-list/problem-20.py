"""
This question is asked by Apple. Given a potentially cyclical linked list where each value is unique, return the node at which the cycle starts. If the list does not contain a cycle, return null.

Ex: Given the following linked lists...

1->2->3, return null
1->2->3->4->5->2 (5 points back to 2), return a reference to the node containing 2
1->9->3->7->7 (7 points to itself), return a reference to the node containing 7
"""

def getStartOfCycle(head):
    if head is None:
        return head
    
    hasCycle = False
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            hasCycle = True
            break

    if hasCycle:
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

    return None