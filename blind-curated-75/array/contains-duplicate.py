class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numCount = {}
        
        for num in nums:
            if num not in numCount:
                numCount[num] = 0
            numCount[num] += 1
            
        return not (len(nums) == len(numCount.keys()))

    def containsDuplicate2(self, nums: List[int]) -> bool:
        return not len(nums) == len(set(nums))