class Solution:
    def __init__(self, nums):
        self.nums = nums

    def checkIfSorted(self):
        nums = self.nums

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return False

        return True

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    S = Solution(nums)
    print(S.checkIfSorted())