n = int(input())

while n != 0:

    values = list(map(int, input().split()))

    maior = values[n * 2 - 1]
    menor = sum(values)

    for i in range(n):

        par = values[i] + values[n * 2 - 1 - i]

        if par > maior:
            maior = par

        if par < menor:
            menor = par

    print("%d %d" % (maior, menor))

    n = int(input())