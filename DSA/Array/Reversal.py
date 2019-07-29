def ArrayReversal(arr):
    mid = len(arr) // 2
    for i in range(mid):
        arr[i], arr[(len(arr) - 1) - i] = arr[(len(arr) - 1) - i], arr[i]
    return arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Before Reversal : " , arr)
    result = ArrayReversal(arr)
    print("After Reversal : " , arr)