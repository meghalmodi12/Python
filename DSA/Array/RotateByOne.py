def RotateByOne(arr):
    lastElement = arr[len(arr) - 1]
    
    for i in range(len(arr) - 1):
        arr[i+1] = arr[i]
    
    arr[0] = lastElement
    return arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Before Rotation : " , arr)
    result = RotateByOne(arr)
    print("After Rotation : " , arr)