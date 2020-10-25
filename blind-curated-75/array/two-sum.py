class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = dict()
        for i in range(len(nums)):
            val = target - nums[i]
            if val in numDict:
                return [numDict[val], i]
            numDict[nums[i]] = i