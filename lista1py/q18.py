# Questao 18
# Escreva um algoritmo para gerar o inverso de um número num 
# com três algarismos (Ex: o inv. de 498 é 894), onde num é uma 
# variável inteira de entrada do programa. 

print("Digite um numero inteiro de três algarismos:")
num = int(input())

# centenas
a = int(num / 100)

aux = num % 100 

# dezenas
b = int(aux / 10)

# unidades
c = aux % 10

inverso = c*100 + b*10 + a

print("Inverso de %d = %d" %(num, inverso))