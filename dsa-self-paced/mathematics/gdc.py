class Solution:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Greatest Common Divisor
    def getGDC(self):
        result = min(self.a, self.b)

        while True:
            if result % self.a == 0 and result % self.b == 0:
                break
            else:
                result += 1

        return result