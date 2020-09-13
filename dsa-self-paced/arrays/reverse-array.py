class Solution:
    def __init__(self, nums):
        self.nums = nums

    def reverse(self):
        nums = self.nums
        start, end = 0, len(nums) - 1

        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        return nums

if __name__ == "__main__":
    nums = [1, 2, 3]
    S = Solution(nums)
    print(S.reverse())
