import sys

class Solution:
    def __init__(self, nums):
        self.nums = nums

    def getMissingNum(self):
        result = 0
        maxNum = -sys.maxsize
        nums = self.nums

        for num in nums:
            result = result ^ num
            maxNum = max(maxNum, num)

        for i in range(1, maxNum + 1):
            result = result ^ i

        return result

    def getMissingNum_2(self):
        maxNum = max(self.nums)
        total = sum(self.nums)
        return ((maxNum * (maxNum + 1)) // 2) - total

if __name__ == "__main__":
    nums = [1, 4, 3]
    S = Solution(nums)
    print(S.getMissingNum_2())