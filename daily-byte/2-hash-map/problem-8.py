"""
This question is asked by Google. Given an array of integers, return whether or not two numbers sum to a given target, k.
Note: you may not sum a number with itself.

Ex: Given the following...

[1, 3, 8, 2], k = 10, return true (8 + 2)
[3, 9, 13, 7], k = 8, return false
[4, 2, 6, 5, 2], k = 4, return true (2 + 2)
"""

def twoSum(nums, target):
    numDict = {}

    for num in nums:
        valueToLook = target - num
        if valueToLook in numDict:
            return True
        numDict[num] = 1

    return False

print(twoSum([1, 3, 8, 2], 10))
print(twoSum([3, 9, 13, 7], 8))
print(twoSum([4, 2, 6, 5, 2], 4))