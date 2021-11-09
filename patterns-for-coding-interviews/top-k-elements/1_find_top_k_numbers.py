from heapq import *

# Maintain a min-heap of size k
def topKNumbers(nums, k):
    minHeap = []

    # Insert first k elements to the heap
    for i in range(k):
        heappush(minHeap, nums[i])

    # For rest of the elements, first remove and then insert to maintain size k
    for i in range(k, len(nums)):
        heappop(minHeap)
        heappush(minHeap, nums[i])

    return minHeap

print(topKNumbers([3, 1, 5, 12, 2, 11], 3))
