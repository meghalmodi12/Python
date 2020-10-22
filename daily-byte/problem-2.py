"""
This question is asked by Facebook. Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

Ex: Given the following strings...
"level", return true
"algorithm", return false
"A man, a plan, a canal: Panama.", return true
"""

def isPalindrome(s):
    left, right = 0, len(s) - 1

    while left <= right:
        if not s[left].isalpha():
            left += 1
        elif not s[right].isalpha():
            right -= 1
        else:
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

    return True