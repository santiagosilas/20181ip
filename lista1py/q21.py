segundos = int(input('segundos:'))

num_horas = int(segundos / 3600)

resto = segundos % 3600

num_mins = int(resto / 60)

num_segundos = resto % 60

print("horas:%d mins:%d, segs:%d" %(num_horas, num_mins, num_segundos))
