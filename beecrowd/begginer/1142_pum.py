def saida(m):
    if m % 4 != 0:
        return str(m)
    else:
        return "PUM"

n = int(input())



for i in range(n):

    inicio = i * 4 + 1

    print(" ".join(map(saida, range(inicio, (inicio + 4)))))