"""
This question is asked by Google. Given a string only containing the following characters (, ), {, }, [, and ] return whether or not the opening and closing characters are in a valid order.

Ex: Given the following strings...

"(){}[]", return true
"(({[]}))", return true
"{(})", return false
"""

def validateCharacters(data):
    stack = []

    for d in data:
        if d in ['(', '{', '[']:
            if d == '(':
                stack.append(')')
            elif d == '{':
                stack.append('}')
            else:
                stack.append(']')
        else:
            if len(stack) == 0 or stack[-1] != d:
                return False
            else:
                stack.pop()

    return len(stack) == 0

print(validateCharacters('(){}[]'))
print(validateCharacters('(({[]}))'))
print(validateCharacters('{(})')) 