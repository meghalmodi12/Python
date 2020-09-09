"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

def findMaxPrimeFactor(number):
    primeNumList = []
    if number > 1:
        while number % 2 == 0:
            primeNumList.append(2)
            number = number / 2

        # number must be odd at this point 
        # so a skip of 2 ( i = i + 2) can be used 
        for i in range(3, int(math.sqrt(number)) + 1, 2):
            if number % i == 0:
                primeNumList.append(i)
                number = number / i

        if number > 2:
            primeNumList.append(number)

    return primeNumList


if __name__ == "__main__":
    number = int(input("Enter Number : "))
    primeNumList = findMaxPrimeFactor(number)
    
    print(primeNumList)
    if primeNumList[-1] != None:
        print(primeNumList[-1])
    else:
        print("No prime factor found")
