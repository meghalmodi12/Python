from MinHeap import MinHeap

def findKSmallest(arr, k):
    result = []
    minHeap = MinHeap()
    minHeap.buildMinHeap(arr)

    while k > 0:
        result.append(minHeap.delete())
        k -= 1

    return result

print(findKSmallest([9, 4, 7, 1, -2, 6, 5], 2))
print(findKSmallest([9, 4, 7, 1, -2, 6, 5], 3))
print(findKSmallest([9, 4, 7, 1, -2, 6, 5], 5))
    