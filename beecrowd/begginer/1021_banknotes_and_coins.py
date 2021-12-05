valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

print("NOTAS:")

for n in notas:
    print("%d nota(s) de R$ %.2f" % (int(valor / n), n))
    valor = round(valor % n, 2)

print("MOEDAS:")

for m in moedas:
    print("%d moeda(s) de R$ %.2f" % (int(valor / m), m))
    valor = round(valor % m, 2)