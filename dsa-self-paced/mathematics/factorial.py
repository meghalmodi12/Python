import math

class Solution:
    def __init__(self, num):
        self.num = num

    # O(n) time, O(1) space
    def factorial(self):
        result = 1

        for i in range(1, self.num + 1):
            result *= i

        return result

    # O(n) time, O(n) space because of function call stack
    def factorialRecursive(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n - 1)

     # O(n) time, O(1)
     # The solution may not work all the time, as few factorial result may be out of integer range
    def trailingZeroInFactorial(self, n):
        result = 0
        fact = self.factorialRecursive(n)

        while fact % 10 == 0:
            fact = fact // 10
            result += 1

        return result

    # O(log n) time, O(1)
    # This solution solves the overflow problem
    def trailingZeroInFactorial_2(self, n):
        result = 0
        start = 5

        while start <= n:
            result += int(math.floor(n/start))
            start *= 5

        return result