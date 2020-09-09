"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sumOfSquares(num):
    if num == 0:
        return num
    else:
        return (num * (num + 1) * ((2 * num) + 1)) / 6

def squareOfSum(num):
    result = 0
    if num == 0:
        return result
    else:
        result = (num * (num + 1)) / 2
        return result * result

if __name__ == "__main__":
    num = int(input("Enter number : "))
    diff = squareOfSum(num) - sumOfSquares(num)
    print("Result : ", int(diff))
