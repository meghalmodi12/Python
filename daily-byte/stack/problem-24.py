"""
This question is asked by Facebook. Given a string s containing only lowercase letters, continuously remove adjacent characters that are the same and return the result.

Ex: Given the following strings...

s = "abccba", return ""
s = "foobar", return "fbar"
s = "abccbefggfe", return "a"
"""

def removeAdjacentDuplicates(s):
    stack = []

    for char in s:
        if len(stack) > 0 and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)

print(removeAdjacentDuplicates('abccba'))
print(removeAdjacentDuplicates('foobar'))
print(removeAdjacentDuplicates('abccbefggfe'))
