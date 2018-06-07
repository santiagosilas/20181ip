nome = input()
salario = float(input())
total_vendas = float(input())

total = salario + 0.15 * total_vendas

print("TOTAL = R$ %.2f" % total)