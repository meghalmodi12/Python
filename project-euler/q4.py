"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindrome(number):
    palindromeNum = 0
    remainder = 0
    originalNum = number

    while originalNum != 0:
        remainder = originalNum % 10
        palindromeNum = (palindromeNum * 10) + remainder
        originalNum = originalNum // 10

    return number == palindromeNum

def getLargestPalindrome():
    largestPalindrome = 0

    for i in range(1, 1000):
        for j in range(1, 1000):
            result = i * j
            if isPalindrome(result):
                if result > largestPalindrome:
                    largestPalindrome = result
    
    return largestPalindrome

    
if __name__ == "__main__":
    print("Largest Palindrome : ", getLargestPalindrome())
