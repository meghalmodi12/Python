class Solution:
    def __init__(self, n):
        self.n = n

    def getSetBitsCount(self):
        result = 0
        n = self.n

        while n > 0:
            n = n & (n-1)
            result += 1
        
        return result

if __name__ == "__main__":
    S = Solution(32)
    print(S.getSetBitsCount())
