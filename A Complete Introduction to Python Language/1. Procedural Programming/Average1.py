numList = []
total = 0
count = 0

def SelectionSort(arr):
    if len(arr):
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
    return arr


while True:
    line = input("Enter a number (Or Enter to finish) : ")
    if line:
        try:
            num = int(line)
            numList.append(num)
        except ValueError as err:
            print(err)
            continue
        total += num
        count += 1
    else:
        break

if count:
    print("Before Sort : " , numList)
    numList = SelectionSort(numList)
    print("After Sort : " , numList)
    if len(numList) % 2 == 0:
        median = (numList[len(numList) // 2] + numList[(len(numList) // 2) + 1]) / 2
    else:
        median = numList[(len(numList) // 2)]

    print("Total : {}, Count : {}, Min : {}, Max : {}, Mean : {}, Median : {}".format(total, count, min(numList), max(numList), total/count, median))