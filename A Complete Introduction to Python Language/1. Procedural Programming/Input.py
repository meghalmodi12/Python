print("Tyep integers, each followed by Enter; Or just hit Enter to finish.")

total = 0
count = 0

while True:
    line = input("Integer: ")
    if line:
        try:
            number = int(line)
        except ValueError as err:
            print(err)
            continue
        total += number
        count += 1
    else:
        break
    
if count:
    print("Total : {}, Count : {}, Mean : {}".format(total, count, total/count))