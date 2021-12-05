from datetime import datetime

bDay = int(input().split()[1])

bh, bm, bs = input().split(":")

bh = int(bh)
bm = int(bm)
bs = int(bs)

fDay = int(input().split()[1])

fh, fm, fs = input().split(":")

fh = int(fh)
fm = int(fm)
fs = int(fs)

bDay = datetime(year=2021, month=4 ,day=bDay, hour=bh, minute=bm, second=bs)
fDay = datetime(year=2021, month=4, day=fDay, hour=fh, minute=fm, second=fs)

dif = fDay - bDay
dif = dif.total_seconds()

if dif < 60:
    dif = 60

day = int(dif / 86400)
aux = dif % 86400

hour = int(aux / 3600)
aux = aux % 3600

min = int(aux / 60)
sec = aux % 60

print("%d dia(s)" % day)
print("%d hora(s)" % hour)
print("%d minuto(s)" % min)
print("%d segundo(s)" % sec)