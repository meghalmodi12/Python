"""
Given an array of sorted numbers and a target sum, 
find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) 
such that they add up to the given target.
"""
def pair_with_targetsum(arr, target_sum):
  left, right = 0, len(arr) - 1

  while left < right:
    if arr[left] + arr[right] == target_sum:
      return [left, right]
    elif arr[left] + arr[right] < target_sum:
      left += 1
    else:
      right -= 1

  return [-1, -1]

def main():
  print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
  print(pair_with_targetsum([2, 5, 9, 11], 11))

main()