class Solution:
    def __init__(self, n):
        self.n = n

    def convertToBinary(self):
        binaryArray = []
        num = self.n

        while num > 0:
            binaryArray.append(num % 2)
            num = num // 2

        return binaryArray

    def checkKthBit(self, k):
        binaryArray = self.convertToBinary()
        return binaryArray[k-1] == 1

class Solution2:
    def __init__(self, n, k):
        self.n = n
        self.k = k

    # Using left shift
    def checkKthBit(self):
        return self.n & (1 << (self.k - 1)) == 1

    # Using right shift
    def checkKthBit_2(self):
        return self.n >> (self.k - 1) & 1 == 1

if __name__ == "__main__":
    S = Solution2(8, 2)
    print(S.checkKthBit())