"""
Given a string with lowercase letters only, 
if you are allowed to replace no more than ‘k’ letters with any letter, 
find the length of the longest substring having the same letters after replacement.
"""

def length_of_longest_substring(str, k):
  charFreq = {}
  windowStart, maxRepeatCharCount, maxLength = 0, 0, 0

  for windowEnd in range(len(str)):
    rightMostChar = str[windowEnd]
    if rightMostChar not in charFreq:
      charFreq[rightMostChar] = 0
    charFreq[rightMostChar] += 1

    maxRepeatCharCount = max(maxRepeatCharCount, charFreq[rightMostChar])

    """
    Current window size is from windowStart to windowEnd, overall we have a letter which is
    repeating 'maxRepeatCharCount' times, this means we can have a window which has one letter
    repeating 'maxRepeatCharCount' times and the remaining letters we should replace.
    if the remaining letters are more than 'k', it is the time to shrink the window as we
    are not allowed to replace more than 'k' letters
    """
    if (windowEnd - windowStart + 1 - maxRepeatCharCount) > k:
      charFreq[str[windowStart]] -= 1
      windowStart += 1

    maxLength = max(maxLength, windowEnd - windowStart + 1)

  return maxLength

def main():
  print(length_of_longest_substring("aabccbb", 2))
  print(length_of_longest_substring("abbcb", 1))
  print(length_of_longest_substring("abccde", 1))

main()
