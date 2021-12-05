m, n = input().split()

m = int(m)
n = int(n)


def maior(m, n):
    return int((m + n + abs(m - n)) / 2)


def menor(m, n):
    return int((m + n - abs(m - n)) / 2)


while m > 0 and n > 0:

    ma = maior(m, n)
    me = menor(m, n)

    saida = []

    for i in range(ma - me + 1):
        saida.append(me + i)

    print(" ".join(map(str, saida)), "Sum=" + str(sum(saida)))

    m, n = input().split()

    m = int(m)
    n = int(n)