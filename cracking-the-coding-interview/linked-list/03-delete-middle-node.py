from LinkedList import LinkedList

class Solution:
    def __init__(self, listItems):
        self.lList = LinkedList()
        self.lList.generate(listItems)

    def deleteMiddleNode(self):
        slow, fast = self.lList.head, self.lList.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        if slow.next: 
            slow.data = slow.next.data
            slow.next = slow.next.next

        self.lList.printList()

if __name__ == "__main__":
    S = Solution([1, 2, 2])
    S.deleteMiddleNode()
