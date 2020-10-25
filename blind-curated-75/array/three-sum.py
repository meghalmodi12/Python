class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        
        for i in range(0, len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                tSum = nums[i] + nums[left] + nums[right]
                if tSum > 0:
                    right -= 1
                elif tSum < 0:
                    left += 1
                else:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    
        return result