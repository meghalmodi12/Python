"""
This question is asked by Microsoft. Given an array of strings, return the longest common prefix that is shared amongst all strings.
Note: you may assume all strings only contain lowercase alphabetical characters.

Ex: Given the following arrays...

["colorado", "color", "cold"], return "col"
["a", "b", "c"], return ""
["spot", "spotty", "spotted"], return "spot"
"""

def longestCommonPrefix(data):
    if len(data) == 0:
            return ""
    if len(data) == 1:
        return data[0]

    minWord = data[0]

    for word in data[1:]:
        if len(word) < len(minWord):
            minWord = word

    minWord = list(minWord)

    for i in range(len(data)):
        if len(minWord) > 0:
            currentWord = data[i]
            mismatchFoundAt = -1
            for j in range(len(minWord)):
                if minWord[j] != currentWord[j]:
                    mismatchFoundAt = j
                    break
            if mismatchFoundAt >= 0:
                minWord = minWord[:mismatchFoundAt]
        else:
            break

    return "".join(minWord)
            
print(longestCommonPrefix(["colorado", "color", "cold"]))
print(longestCommonPrefix(["a", "b", "c"]))  
print(longestCommonPrefix(["spot", "spotty", "spotted"]))         