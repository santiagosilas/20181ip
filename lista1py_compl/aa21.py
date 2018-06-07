valor = float(input())

notas = int(valor)
moedas = (valor - int(valor))

n100 = int(notas/100)
resto = notas % 100
n50 = int(resto / 50)
resto = resto % 50
n20 = int(resto / 20)
resto = resto % 20
n10 = int(resto / 10)
resto = resto % 10
n5 = int(resto / 5)
resto = resto % 5
n2 = int(resto / 2)
resto = resto % 2

resto = int(100 * (resto + moedas))

m100 = int(resto/100)
resto = resto % 100
m50 = int(resto / 50)
resto = resto % 50
m25 = int(resto / 20)
resto = resto % 20
m10 = int(resto / 10)
resto = resto % 10
m5 = int(resto / 5)
m1 = resto % 5

print("NOTAS:")
print("%d 5 nota(s) de R$ 100.00"  % n100 )
print("%d 1 nota(s) de R$ 50.00"   %  n50 )
print("%d 1 nota(s) de R$ 20.00"   %  n20)
print("%d 0 nota(s) de R$ 10.00"   %  n10)
print("%d 1 nota(s) de R$ 5.00"    %   n5)
print("%d 0 nota(s) de R$ 2.00"    %   n2)
print("MOEDAS:")
print("%d 1 moeda(s) de R$ 1.00"  %  m100)
print("%d 1 moeda(s) de R$ 0.50"  %  m50)
print("%d 0 moeda(s) de R$ 0.25"  %  m25)
print("%d 2 moeda(s) de R$ 0.10"  %  m10)
print("%d 0 moeda(s) de R$ 0.05"  %  m5)
print("%d 3 moeda(s) de R$ 0.01"  %  m1)
