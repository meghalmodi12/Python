numList = []
total = 0
count = 0

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
    print(numList)
    print("Total : {}, Count : {}, Min : {}, Max : {}, Mean : {}".format(total, count, min(numList), max(numList), total/count))