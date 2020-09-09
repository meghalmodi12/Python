"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def findSmallestNumDivisible(num):
    counter = 1
    numberFound = False
    while not numberFound:
        sumRemainder = 0
        for i in range(1, num + 1):
            sumRemainder += counter % i
            if sumRemainder > 0:
                break
        
        if sumRemainder == 0:
            numberFound = True
        else:
            counter += 1
    return counter

if __name__ == "__main__":
    num = int(input("Enter Number : "))
    print(findSmallestNumDivisible(num))