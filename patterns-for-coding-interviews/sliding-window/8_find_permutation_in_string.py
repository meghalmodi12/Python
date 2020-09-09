"""
Given a string and a pattern, find out if the string contains any permutation of the pattern.
Permutation is defined as the re-arranging of the characters of the string. For example, 
“abc” has the following six permutations:
- abc
- acb
- bac
- bca
- cab
- cba
If a string has ‘n’ distinct characters it will have n!n! permutations.
"""
def find_permutation(str, pattern):
  patternFreq = {}
  matchCount, windowStart = 0, 0

  for p in pattern:
    if p not in patternFreq:
      patternFreq[p] = 0
    patternFreq[p] += 1

  for windowEnd in range(len(str)):
    rightChar = str[windowEnd]
    if rightChar in patternFreq:
      patternFreq[rightChar] -= 1
      if patternFreq[rightChar] == 0:
        matchCount += 1

    if matchCount == len(patternFreq):
      return True

    if windowEnd >= len(pattern) - 1:
      leftChar = str[windowStart]
      windowStart += 1
      if leftChar in patternFreq:
        if patternFreq[leftChar] == 0:
          matchCount -= 1
        patternFreq[leftChar] += 1

  return False

def main():
  print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
  print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
  print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
  print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))

main()
