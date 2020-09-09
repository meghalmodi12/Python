class Solution:
    def __init__(self, num):
        self.num = num
        self.revNum = 0

    # O(n) time, O(1) space
    def isPalindromeNumber(self):
        n = self.num

        while n > 0:
            rem = n % 10
            n = n // 10
            self.revNum = self.revNum * 10 + rem

        return self.revNum == self.num