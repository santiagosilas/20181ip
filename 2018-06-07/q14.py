# Elabore um algoritmo que permita 
# a entrada de horas de início e 
# término (hh:mm) de uma palestra, 
# exibindo a quantidade de horas e 
# minutos.

# inicio
hi = int( input() ) 
mi = int( input() )

#termino
hf = int(input())
mf = int(input())

# converter para minutos
inicio = hi * 60 + mi
termino = hf * 60 + mf

diff = termino - inicio

h = diff // 60
m = diff % 60
print("%.2d horas e %.2d mins." %(h, m) )


