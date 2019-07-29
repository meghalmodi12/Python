def ReverseString(arr, start_index, end_index):
    if start_index >= end_index:
        return
    ReverseString(arr, start_index + 1, end_index - 1)
    
    temp = arr[start_index]
    arr[start_index] = arr[end_index]
    arr[end_index] = temp

if __name__ == "__main__":
    arr = ['M', 'e', 'g', 'h', 'a', 'l']
    ReverseString(arr, 0, len(arr) - 1)
    print(arr)