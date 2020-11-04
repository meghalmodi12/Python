"""
This question is asked by Apple. Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string).
Note: neither binary string will contain leading 0s unless the string itself is 0

Ex: Given the following binary strings...

"100" + "1", return "101"
"11" + "1", return "100"
"1" + "0", return  "1"
"""

def addBinary(s1, s2):
    result = []
    carry = '0'

    s1, s2 = list(s1), list(s2)

    while s1 or s2:
        val1 = '0'
        val2 = '0'

        if s1 and s2:
            val1 = s1.pop()
            val2 = s2.pop()
        elif not s2:
            val1 = s1.pop()
        else:
            val2 = s2.pop()

        if val1 == '1' and val2 == '1':
            result.append('0')
            carry = '1'
        elif val1 == '0' and val2 == '0':
            if carry == '1':
                result.append('1')
            else:
                result.append('0')
            carry = '0'
        else:
            if carry == '1':
                result.append('0')
            else:
                result.append('1')

    if carry == '1':
        result = ['1'] + result

    return "".join(result)

print(addBinary('100', '1'))
print(addBinary('11', '1'))
print(addBinary('1', '0'))