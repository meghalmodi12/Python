def SelectionSort(arr, start_index, end_index):
    if start_index >= end_index:
        return

    min_index = getMinIndex(arr, start_index, end_index)

    temp = arr[min_index]
    arr[start_index] = arr[min_index]
    arr[min_index] = temp

    SelectionSort(arr, start_index + 1, end_index)

def getMinIndex(arr, start_index, end_index):
    minIndex = 0
    temp = arr[start_index]
    for i in range(start_index, end_index):
        if arr[i] < temp:
            temp = arr[i]
            minIndex = i
    return minIndex

if __name__ == "__main__":
    arr = [1, 3, 4, 5, 2, 10]
    SelectionSort(arr, 0, len(arr) - 1)
    print(arr)