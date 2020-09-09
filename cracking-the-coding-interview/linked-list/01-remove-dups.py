from LinkedList import LinkedList

class Solution:
    def __init__(self, listItems):
        self.lList = LinkedList()
        self.lList.generate(listItems)

    def removeDuplicates(self):
        if self.lList.head is None:
            return
        
        start = self.lList.head
        seen = set([start.data])

        while start.next:
            if start.next.data in seen:
                start.next = start.next.next
            else:
                seen.add(start.next.data)
                start = start.next

        self.lList.printList()

    def removeDuplicates_2(self):
        if self.lList.head is None:
            return
        
        curr = self.lList.head
        while curr:
            start = curr
            while start.next:
                if start.next.data == curr.data:
                    start.next = start.next.next
                else:
                    start = start.next
            curr = curr.next

        self.lList.printList()

if __name__ == "__main__":
    S = Solution([1, 2, 1, 2, 3])
    S.removeDuplicates_2()