"""
Merge K sorted arrays
"""

import heapq

class Node:
    def __init__(self, arrayIndex, itemIndex, value):
        self.arrayIndex = arrayIndex
        self.itemIndex = itemIndex
        self.value = value

    def __lt__(self, otherNode):
        return self.value < otherNode.value

def mergeKSortedArrays(arrays):
    result = []
    minHeap = []

    for i in range(len(arrays)):
        node = Node(i, 0, arrays[i][0])
        heapq.heappush(minHeap, node)

    while len(minHeap):
        current = heapq.heappop(minHeap)
        arrIdx = current.arrayIndex
        itemIdx = current.itemIndex

        if itemIdx + 1 < len(arrays[arrIdx]):
            tempNode = Node(arrIdx, itemIdx + 1, arrays[arrIdx][itemIdx + 1])
            heapq.heappush(minHeap, tempNode)

        result.append(current.value)

    return result

arrInput = [[3, 5, 7], [0, 6], [0, 6, 28]]
result = mergeKSortedArrays(arrInput)

# print(result)

