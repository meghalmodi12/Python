def SelectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                min_idx = j
        arr