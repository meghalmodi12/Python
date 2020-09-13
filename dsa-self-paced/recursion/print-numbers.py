class Solution:
    def print1toN(self, num):
        if num == 0:
            return
        self.print1toN(num - 1)
        print(num, end = ' ')

    def printNto1(self, num):
        if num == 0:
            return
        print(num, end = ' ')
        self.printNto1(num - 1)

if __name__ == "__main__":
    S = Solution()
    S.print1toN(10)
    S.printNto1(10)