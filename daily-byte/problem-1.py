"""
This question is asked by Google. Given a string, reverse all of its characters and return the resulting string.
Ex: Given the following strings...

“Cat”, return “taC”
“The Daily Byte”, return "etyB yliaD ehT”
“civic”, return “civic”
"""

def reverseString(s):
    s = s.split("")
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]

    return "".join(s)