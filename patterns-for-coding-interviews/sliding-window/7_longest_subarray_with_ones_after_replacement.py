"""
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, 
find the length of the longest contiguous subarray having all 1s.
"""
def length_of_longest_substring(arr, k):
  numFrequency   = {}
  windowStart, maxLength, maxCountOfOne = 0, 0, 0

  for windowEnd in range(len(arr)):
    if arr[windowEnd] == 1:
      maxCountOfOne += 1

    if (windowEnd - windowStart + 1 - maxCountOfOne) > k:
      if arr[windowStart] == 1:
        maxCountOfOne -= 1
      windowStart += 1

    maxLength = max(maxLength, windowEnd - windowStart + 1)

  return maxLength

def main():
  print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
  print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))

main()