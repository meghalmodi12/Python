"""
This question is asked by Amazon. Given two arrays of numbers, where the first array is a subset of the second array, return an array containing all the next greater elements for each element in the first array, in the second array. If there is no greater element for any element, output -1 for that number.

Ex: Given the following arrays…

nums1 = [4,1,2], nums2 = [1,3,4,2], return [-1, 3, -1] because no element in nums2 is greater than 4, 3 is the first number in nums2 greater than 1, and no element in nums2 is greater than 2.
nums1 = [2,4], nums2 = [1,2,3,4], return [3, -1] because 3 is the first greater element that occurs in nums2 after 2 and no element is greater than 4.
"""

def greaterElements(nums1, nums2):
    nextGreatest = {}
    stack = []
    
    """
    Example:
    nums1 = [1,3,5,2,4]
    nums2 = [6,5,4,3,2,1,7]
    
    Loop through nums2
    1. Check if top of the stack is less then current num
        1A. If yes we have found next greater element for element seting at top of the stack
        1B. Update the hash map with our findings
    2. Append current number to the stack
    """
    for num in nums2:
        while stack and stack[-1] < num:
            nextGreatest[stack.pop()] = num
        stack.append(num)
        
    """
    Loop through nums1
    1. Get associated value or -1
    """      
    for i in range(len(nums1)):
        nums1[i] = nextGreatest.get(nums1[i], -1)
            
    return nums1