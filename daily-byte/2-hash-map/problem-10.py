"""
This question is asked by Facebook. Given two strings s and t return whether or not s is an anagram of t.
Note: An anagram is a word formed by reordering the letters of another word.

Ex: Given the following strings...

s = "cat", t = "tac", return true
s = "listen", t = "silent", return true
s = "program", t = "function", return false
"""

def validateAnagram(s, t):
    if len(s) != len(t):
        return False

    charDict = {}
    for char in s:
        if char not in charDict:
            charDict[char] = 0
        charDict[char] += 1

    for char in t:
        if char not in charDict:
            return False
        elif charDict[char] == 1:
            del charDict[char]
        else:
            charDict[char] -= 1

    return len(charDict) == 0

print(validateAnagram('cat', 'tac'))
print(validateAnagram('listen', 'silent'))
print(validateAnagram('program', 'function'))