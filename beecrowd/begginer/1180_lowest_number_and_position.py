n = int(input())

v = input().split()

for i in range(len(v)):
    v[i] = int(v[i])

m = v[0]
p = 0

for i in range(len(v)):

    if v[i] < m:
        m = v[i]
        p = i

print("Menor valor:", str(m))
print("Posicao:", str(p))