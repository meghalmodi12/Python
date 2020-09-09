import math

class Solution:
    def __init__(self, num):
        self.num = num

    # O(n) time
    def isPrime(self):
        n = self.num

        if n == 1:
            return False
        
        for i in range(2, n):
            if n % i == 0:
                return False

        return True

    # O(sqrt(n)) time
    def isPrime_2(self):
        n = self.num

        if n == 1:
            return False

        i = 2
        nSqrt = math.ceil(math.sqrt(n))

        while i <= nSqrt:
            if n % i == 0:
                return False
            i += 1

        return True

    # Most efficient solution so far
    def isPrime_3(self, newNum = None):
        n = self.num if newNum is None else newNum

        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        i = 5
        nSqrt = math.ceil(math.sqrt(n))

        while i <= nSqrt:
            if n % i == 0 or n % (i+2) == 0:
                return False
            i += 6

        return True

    def getPrimeFactors(self):
        result = []
        n = self.num

        i = 2
        nSqrt = int(math.sqrt(n))

        while i <= nSqrt:
            self.num = i
            if self.isPrime():
                x = i
                while n % x == 0:
                    result.append(i)
                    x = x * i
            i += 1

        if len(result) == 0:
            result.append(n)

        return result

    def countPrimes(self):
        n = self.num
        nSqrt = int(math.sqrt(n))
        primeArr = [True] * (n + 1)
        result = []

        i = 2
        while i <= nSqrt:
            if self.isPrime_3(i):
                j = 2 * i
                while j <= n:
                    primeArr[j] = False
                    j += i
            i += 1

        for i in range(2, n + 1):
            if primeArr[i]:
                result.append(i)

        return result

if __name__ == "__main__":
    S = Solution(100)
    print(S.countPrimes())
