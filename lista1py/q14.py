hi,mi,hf,mf = 10, 25, 11, 30

# converte tempo horas/minutos para minutos
i = hi * 60 + mi
f = hf * 60 + mf

# diferenca em minutos
diff = f - i

# converte minutos para horas e minutos
h = int(diff / 60)
m = diff % 60

print('%.2d:%.2d' %(h, m))