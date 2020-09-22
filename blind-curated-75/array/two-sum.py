"""
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

def TwoSum(arr, target):    
    for i in arr:
        number = target - i
        if number in arr:
            return [i, number]

result = TwoSum([2, 7, 11, 15], 9) 
print(result)
