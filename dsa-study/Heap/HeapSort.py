from MaxHeap import MaxHeap 

def heapSort(nums):
    result = None
    heap = MaxHeap()

    for num in nums:
        heap.insert(num)

    for _ in range(len(nums)):
        heap.delete()

    result = heap.heapList[1:]
    return result

print(heapSort([1, 5, 6, 10, 2, -1, 4, 50, 21]))