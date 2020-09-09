from LinkedList import LinkedList

class Solution:
    def __init__(self, listItems):
        self.lList = LinkedList()
        self.lList.generate(listItems)
        self.lListLength = self.getLength()

    def getLength(self):
        if self.lList.head is None:
            return

        counter = 0
        start = self.lList.head
        while start:
            start = start.next
            counter += 1

        return counter

    def getKthFromLast(self, k):
        if k > self.lListLength:
            return -1

        counter = 0
        slow, fast = self.lList.head, self.lList.head


        while fast is not None:
            if counter >= k:
                slow = slow.next
            fast = fast.next
            counter += 1

        return slow.data

if __name__ == "__main__":
    S = Solution([1, 2, 3, 4, 5, 6, 7, 8])
    result = S.getKthFromLast(5)
    print(result)
