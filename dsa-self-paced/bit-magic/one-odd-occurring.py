class Solution:
    def __init__(self, nums):
        self.nums = nums

    def getOddOccurringNumber(self):
        result = 0
        nums = self.nums

        for num in nums:
            result = result ^ num

        return result

if __name__ == "__main__":
    nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4]
    S = Solution(nums)
    print(S.getOddOccurringNumber())