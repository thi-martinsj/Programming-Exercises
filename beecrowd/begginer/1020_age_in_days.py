dias = int(input())

meses, anos = 0, 0

anos = int(dias / 365)

dias = dias % 365

meses = int(dias / 30)

dias = dias % 30

print("%d ano(s)" %anos)
print("%d mes(es)" %meses)
print("%d dia(s)" %dias)