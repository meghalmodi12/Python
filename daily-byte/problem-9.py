"""
This question is asked by Amazon. Given a string representing your stones and another string representing a list of jewels, return the number of stones that you have that are also jewels.

Ex: Given the following jewels and stones...

jewels = "abc", stones = "ac", return 2
jewels = "Af", stones = "AaaddfFf", return 3
jewels = "AYOPD", stones = "ayopd", return 0
"""

def getNumOfStones(jewels, stones):
    result = 0
    jewelDict = {}

    for jewel in jewels:
        if jewel not in jewelDict:
            jewelDict[jewel] = 0

    for stone in stones:
        if stone in jewelDict:
            result += 1

    return result

print(getNumOfStones('abc', 'ac'))
print(getNumOfStones('Af', 'AaaddfFf'))
print(getNumOfStones('AYOPD', 'ayopd'))