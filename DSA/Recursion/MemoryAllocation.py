def printFun(num):
    if num < 1:
        return
    else:
        print(num)
        printFun(num -1)
        print(num)

if __name__ == "__main__":
    num = 2
    printFun(num)