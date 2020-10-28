"""
This question is asked by Microsoft. Given a string, return the index of its first unique character. If a unique character does not exist, return -1.

Ex: Given the following strings...

"abcabd", return 2
"thedailybyte", return 1
"developer", return 0
"""

def firstUniqueCharacter(s):
    charDict = {}

    for char in s:
        if char not in charDict:
            charDict[char] = 0
        charDict[char] += 1

    for i in range(len(s)):
        if charDict[s[i]] == 1:
            return i

    return -1

print(firstUniqueCharacter('abcabd'))
print(firstUniqueCharacter('thedailybyte'))
print(firstUniqueCharacter('developer'))