import math

class Solution:
    def __init__(self, num):
        self.num = num

    def getDivisors(self):
        result = []
        n = self.num
        
        for i in range(1, n + 1):
            if n % i == 0:
                result.append(i)

        return result

    def getDivisors_2(self):
        result = []
        n = self.num

        i = 1
        nSqrt = int(math.sqrt(n))

        while i <= nSqrt:
            if n % i == 0:
                if n / i == i:
                    result.append(i)
                else:
                    result.append(i)
                    result.append(n / i)
            i += 1

        return result