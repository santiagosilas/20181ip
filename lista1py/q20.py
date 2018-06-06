# Escreva um algoritmo que converta um intervalo de tempo dado em 
# minutos para horas, minutos, segundos e milissegundos. 
# Exemplo: se o tempo dado for 145,87 min, o programa deve fornecer 
# 2 h 25 min 52s e 200 ms. Obs: 1s = 1000ms.

print("Digite um valor real de minutos:")
minutos = float(input())

# converte minutos para segundos (1 min = 60 segundos, 1s = 1000 ms)
segundos = minutos * 60

num_ms = (segundos - int(segundos) ) * 1000

segundos = int(segundos)

# quantas horas ?
num_hs = int(segundos/3600)

resto_em_segundos = segundos % 3600

# quantos minutos ?
num_mins = int(resto_em_segundos / 60)

num_segs = resto_em_segundos % 60

print(num_hs, num_mins, num_segs, num_ms)