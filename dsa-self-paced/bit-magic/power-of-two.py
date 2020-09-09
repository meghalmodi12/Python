class Solution:
    def __init__(self, n):
        self.n = n

    def isPowerOfTwo(self):
        n = self.n
        if n == 0:
            return False
        return n & (n-1) == 0

if __name__ == "__main__":
    S = Solution(1)
    print(S.isPowerOfTwo())

