"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def findMultiples(num):
    result = 0
    for i in range(num):
        if (i % 3 == 0 or i % 5 == 0):
            result += i
    return result

def findMultiples_2(num):
    result = sumDivisibleBy(3, num - 1) + sumDivisibleBy(5, num - 1) - sumDivisibleBy(15, num - 1)
    return result

def sumDivisibleBy(num, numUpperRange):
    numOfMultiples = int(numUpperRange / num)
    return num * ((numOfMultiples * (numOfMultiples + 1))/2)

if __name__ == "__main__":

    """
    For function : findMultiples
    """
    num = int(input("Enter number : "))
    result = findMultiples(num)
    print("Result For 1st Function : ", int(result))
    

    """
    For function : findMultiples_2
    """
    result = findMultiples_2(num)
    print("Result For 2nd Function : ", int(result))
    