hi, mi, hf, mf = input().split()

hi = float(hi)
mi = float(mi)
hf = float(hf)
mf = float(mf)

minH = mi + hi * 60
minF = mf + (hf + 24) * 60

dif = minF - minH

h = int(dif / 60)
m = dif % 60

if h == 0 and m == 0:
    h = 24

if h >= 24 and m > 0:
    h -= 24

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(h, m))