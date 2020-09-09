"""
Given a string, find the length of the longest substring which has no repeating characters.
"""

import sys
def non_repeat_substring(s):
  maxLength = -sys.maxsize
  windowStart = 0
  charIndexTracker = {}

  for windowEnd in range(len(s)):
    rightMostChar = s[windowEnd]
    if rightMostChar in charIndexTracker:
      """
      this is tricky; in the current window, we will not have any 'rightMostChar' after its previous index
      and if 'windowStart' is already ahead of the last index of 'rightMostChar', we'll keep 'windowStart'
      """
      windowStart = max(windowStart, charIndexTracker[rightMostChar] + 1)
    charIndexTracker[rightMostChar] = windowEnd

    maxLength = max(maxLength, windowEnd - windowStart + 1)

  return maxLength

def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))

main()