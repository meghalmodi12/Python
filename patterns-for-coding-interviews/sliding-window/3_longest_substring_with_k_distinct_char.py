"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.
"""

import sys
def longest_substring_with_k_distinct(str, k):
  maxLength = -sys.maxsize
  charFreq = {}
  windowStart = 0

  for i in range(len(str)):
    if str[i] not in charFreq:
      charFreq[str[i]] = 0
    charFreq[str[i]] += 1

    while len(charFreq.keys()) > k:
      if charFreq[str[windowStart]] == 1:
        del charFreq[str[windowStart]]
      else:
        charFreq[str[windowStart]] -= 1
      windowStart += 1

    maxLength = max(maxLength, sum(charFreq.values()))
  
  return maxLength

def main():
  print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()