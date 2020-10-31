def minHeapify(i, arr):
    left = (2 * i) + 1
    right = (2 * i) + 2
    smallest = i

    if left < len(arr) and arr[left] < arr[smallest]:
        smallest = left

    if right < len(arr) and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        minHeapify(smallest, arr)

def convertMaxHeapToMinHeap(maxHeap):
    for i in range(len(maxHeap) - 1, -1, -1):
        minHeapify(i, maxHeap)
    return maxHeap

print(convertMaxHeapToMinHeap([9, 4, 7, 1, -2, 6, 5]))
print(convertMaxHeapToMinHeap([16, 15, 14, 12, 4, 7, 9, 2, 3, 1]))