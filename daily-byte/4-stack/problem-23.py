"""
This question is asked by Amazon. Given two strings s and t, which represents a sequence of keystrokes, where # denotes a backspace, return whether or not the sequences produce the same result.

Ex: Given the following strings...

s = "ABC#", t = "CD##AB", return true
s = "como#pur#ter", t = "computer", return true
s = "cof#dim#ng", t = "code", return false
"""

def compareKeystrokes(S, T):
    stackS, stackT = [], []

    for char in S:
        if char == '#':
            if len(stackS) > 0:
                stackS.pop()
        else:
            stackS.append(char)

    for char in T:
        if char == '#':
            if len(stackT) > 0:
                stackT.pop()
        else:
            stackT.append(char)

    return "".join(stackS) == "".join(stackT)

print(compareKeystrokes('ABC#','CD##AB'))
print(compareKeystrokes('como#pur#ter','computer'))
print(compareKeystrokes('cof#dim#ng','code'))