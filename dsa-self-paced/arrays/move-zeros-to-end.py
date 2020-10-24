"""
- Init start at 0 
- Start traversal and see if the element at index i is not zero
- If the element is not zero, move it to the start and increment start
- At this point we have moved all non-zero elements
- Now from start to end of the array, replace element at the start with zero
"""

def moveZerosToEnd(nums):
    start = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[start] = nums[i]
            start += 1

    for j in range(start, len(nums)):
        nums[j] = 0

    return nums