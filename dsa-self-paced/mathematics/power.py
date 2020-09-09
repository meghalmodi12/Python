class Solution:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def getPOW(self):
        if self.n == 0:
            return 1
        if self.n == 1:
            return self.x

        result = self.x

        for i in range(1, self.n):
            result *= self.x

        return result

if __name__ == "__main__":
    S = Solution(2, 3)
    print(S.getPOW())