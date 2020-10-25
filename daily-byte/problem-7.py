"""
This question is asked by Facebook. Given a string and the ability to delete at most one character, return whether or not it can form a palindrome.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

Ex: Given the following strings...

"abcba", return true
"foobof", return true (remove the first 'o', the second 'o', or 'b')
"abccab", return false
"""

"""
- Start comparing first and last characters
- If they match -> pass
- Else 
    remove left char to see if the string is palindrome
    remove right char to see if the string is palindrome
    If one of above two passes return true, otherwise return false
- If you have passed the entire string it means it was palindrome initially 
"""

def isPalindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    
    return True

def validatePalindrome(s):
    if len(s) < 2:
        return True

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            r1 = isPalindrome(s, left + 1, right)
            r2 = isPalindrome(s, left, right - 1)
            return  r1 or r2
        
        left += 1
        right -= 1

    return True

print(validatePalindrome('abcba'))
print(validatePalindrome('foobof'))
print(validatePalindrome('abccab'))


        