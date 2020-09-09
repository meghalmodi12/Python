"""
Given an array of positive numbers and a positive number ‘S’, 
find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
Return 0, if no such subarray exists.
"""

import sys
def smallest_subarray_with_given_sum(s, arr):
  if len(nums) == 0:
    return 0
        
  if sum(nums) < s:
    return 0
        
  windowStart = 0
  windowSize = sys.maxsize
  windowSum = 0

  for windowEnd in range(len(nums)):
    windowSum += nums[windowEnd]

    if windowSum >= s:
      while windowSum - nums[windowStart] >= s:
        windowSum -= nums[windowStart]
        windowStart += 1
      windowSize = min(windowSize, windowEnd - windowStart + 1)

  return windowSize

def main():
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()