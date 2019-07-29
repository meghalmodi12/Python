# Accessing string character using indexing
str = "Meghal"
print(str[1])

# Attempting to modify part of string to prove strings are immutable
# str[1] = 'E'

# Object reference
x = 'red'
y = 'green'
z = x
print(x, y, z)

# type of object
name = 'Meghal'
print(name, type(name))

name = ['M', 'e', 'g', 'h', 'a', 'l']
print(name, type(name))

# list append
lst = [1, 2, 3, 'Jinal']
# list.append() will return none so we can not assign that to lst
# lst = list.append(lst, 'Meghal')
list.append(lst, 'Meghal')
print(lst)
lst = lst + ['House']
print(lst)