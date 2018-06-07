import math
x = float(input())
u = float(input())
o = float(input())
a = 2 * math.pow(o, 2)
b = -1 * math.pow((math.log(x) - u, 2))
c = b / a
d = (x * o * math.sqrt(2 * math.pi)) ** -1
f = d * c

