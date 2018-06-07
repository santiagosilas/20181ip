A = int(input())
n100 = int(A/100)

resto = A % 100

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

n1 = resto

print("%d" % A )
print("%d nota(s) de R$ 100,00" % n100 )
print("%d nota(s) de R$ 50,00" % n50 )
print("%d nota(s) de R$ 20,00" % n20 )
print("%d nota(s) de R$ 10,00" % n10 )
print("%d nota(s) de R$ 5,00" % n5 )
print("%d nota(s) de R$ 2,00" % n2 )
print("%d nota(s) de R$ 1,00" % n1 )
