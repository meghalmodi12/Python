"""
- One pass solution
- Init the largest and second largest variables with -infinite value
- If num[i] is greater than largest
    - Assign largest to second largest
    - Assign num[i] to largest
  Else If  nums[i] > second largest and num[i] is not equal to the largest
    - Assign num[i] to second largest
- Return second largest 
"""

def getSecondLargest(nums):
    maxNum, sencondMaxNum = -sys.maxsize, -sys.maxsize

    for i in range(len(nums)):
        if nums[i] > maxNum:
            sencondMaxNum = maxNum
            maxNum = nums[i]
        elif nums[i] > sencondMaxNum and nums[i] != maxNum:
            sencondMaxNum = nums[i]

    return sencondMaxNum