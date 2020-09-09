class Solution:
    def __init__(self, num):
        self.num = num

    # O(n) time, O(1) space
    def countDigits(self):
        n = self.num
        result = 0

        while n > 0:
            n = n // 10
            result += 1

        return result