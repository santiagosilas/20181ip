"""
_________________________________________________________
a| 2    | 2 + 3 = 5   |    5         | 5 - 2 = 3   | 3   |
b| 3    |   3         | 5 - 3 = 2    |    2        | 2   |
"""

a = int(input('digite a:'))
b = int(input('digite b:'))

print("a:%d b:%d" %(a, b))

a = a + b
print("a:%d b:%d" %(a, b))

b = a - b
print("a:%d b:%d" %(a, b))

a = a - b
print("a:%d b:%d" %(a, b))