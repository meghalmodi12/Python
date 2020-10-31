"""

MinHeap Data Structure
- Represented as a complete binary tree or almost complete binary tree
- We can use array to store data
- If i is the parent node
    - Left child is stored at 2 * i index
    - Right child is stored at (2 * i) + 1 index
- For any node i its parent is stored at Floor(i / 2) index
- Insert operation always happens at leaf node (end of the list) with time complexcity O(log n)
    - Insert new value at the end of the list
    - Increase size of the list
    - Check if the value is lesser than its parent's
    - If true, swap the value with its parent
    - Repeat until true
- Delete operation always happens at root node (beginning of the list) with time complexcity O(log n)
    - Replace the value at root with last element of the list
    - Shrik the size of the list by one
    - Check if the value is greater than the left or the right child
    - If true, find the maximum of left and right child and replace it with current value
    - Repeat until true

Heapify Process
- Add value from array to the heap list
- Start from the end of the list
    - Get left and right child
    - Compare current index value with left and right child to get the minimum value
    - If the minimum value is not at ith index, perform the swap
    - Repeat the process until Heap starting from ith index is not balanced
    
"""

class MinHeap:
    def __init__(self):
        self.heapList = [0]
        self.heapSize = 0

    def insert(self, value):
        self.heapList.append(value)
        self.heapSize += 1
        self.moveUp()

    def moveUp(self):
        i = self.heapSize

        while i // 2 > 0:
            parent = i // 2

            if self.heapList[i] < self.heapList[parent]:
                self.heapList[i], self.heapList[parent] = self.heapList[parent], self.heapList[i]
                i = parent
            else:
                break

    def delete(self):
        lastElementIdx = self.heapSize
        self.heapList[1], self.heapList[lastElementIdx] = self.heapList[lastElementIdx], self.heapList[1]
        self.heapSize -= 1
        self.moveDown()
        return self.heapList[lastElementIdx]

    def getChildWithMinValue(self, i):
        left = 2 * i
        right = (2 * i) + 1

        if right > self.heapSize:
            return left

        if self.heapList[left] < self.heapList[right]:
            return left
        else:
            return right

    def moveDown(self):
        i = 1

        while (2 * i) <= self.heapSize:
            idxToReplace = self.getChildWithMinValue(i)

            if self.heapList[i] > self.heapList[idxToReplace]:
                self.heapList[i], self.heapList[idxToReplace] = self.heapList[idxToReplace], self.heapList[i]
                i = idxToReplace
            else:
                break

    def buildMinHeap(self, arr):
        for num in arr:
            self.heapList.append(num)
            self.heapSize += 1

        for i in range(self.heapSize, 0, -1):
            self.minHeapify(i)

    def minHeapify(self, i):
        left = (2 * i)
        right = (2 * i) + 1
        smallest = i

        if left <= self.heapSize and self.heapList[left] < self.heapList[smallest]:
            smallest = left

        if right <= self.heapSize and self.heapList[right] < self.heapList[smallest]:
            smallest = right

        if smallest != i:
            self.heapList[i], self.heapList[smallest] = self.heapList[smallest], self.heapList[i]
            self.minHeapify(smallest)
