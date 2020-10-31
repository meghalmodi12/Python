from MaxHeap import MaxHeap


def findKLargest(arr, k):
    result = []
    maxHeap = MaxHeap()
    maxHeap.buildMaxHeap(arr)

    while k > 0:
        result.append(maxHeap.delete())
        k -= 1

    return result

print(findKLargest([9, 4, 7, 1, -2, 6, 5], 2))
print(findKLargest([9, 4, 7, 1, -2, 6, 5], 3))
print(findKLargest([9, 4, 7, 1, -2, 6, 5], 5))