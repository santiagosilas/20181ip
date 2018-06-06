# Questao 15
import math

print("Digite x:")
x = float(input())

aux1 = 1 / math.sqrt(2 * math.pi)

aux2 = -1 * math.pow(x, 2) / 2

aux3 = math.pow(math.e, aux2)

y = aux1 * aux3

print('f(%.2f) = %.4f' %(x, y)) 

