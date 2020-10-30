"""
This question is asked by Google. Given two integer arrays, return their intersection.
Note: the intersection is the set of elements that are common to both arrays.

Ex: Given the following arrays...

nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []
"""

def intersectionOfNumbers(nums1, nums2):
    numDict = {}
    result = []

    for num in nums2:
        if num not in numDict:
            numDict[num] = 0

    for num in nums1:
        if num in numDict:
            result.append(num)
            del numDict[num]
    
    return result

print(intersectionOfNumbers([2, 4, 4, 2], [2, 4]))
print(intersectionOfNumbers([1, 2, 3, 3], [3, 3]))
print(intersectionOfNumbers([2, 4, 6, 8], [1, 3, 5, 7]))