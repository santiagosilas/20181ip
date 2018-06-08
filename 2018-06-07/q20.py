t = float(input()) # 145.87
h = t // 60 # 2h
resto = t % 60 # 25.87
minutos = int(resto) # 25
resto = (resto - minutos) * 60 # 52.2
segundos = int(resto) # 52
ms = int( (resto - segundos ) * 1000)
print("%d %d %d %d" %(h, minutos, segundos, ms))
