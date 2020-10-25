"""
This question is asked by Google. Given a string, return whether or not it uses capitalization correctly. A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.
Ex: Given the following strings...

"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true
"""

def isValidWord(word):
    if len(word) < 2:
        return True

    isCapitalWord = word[0].isupper() and word[1].isupper()
    isValid = True

    for i in range(2, len(word)):
        if isCapitalWord:
            isValid = isValid and word[i].isupper()
        else:
            isValid = isValid and word[i].islower()

        if not isValid:
            return isValid

    return isValid

print(isValidWord('USA'))
print(isValidWord('Calvin'))
print(isValidWord('compUter'))
print(isValidWord('coding'))
    
