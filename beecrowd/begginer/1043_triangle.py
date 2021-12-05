a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

if abs(b-c) < a < (b+c):
    print("Perimetro = %.1f" % (a+b+c))
else:
    print("Area = %.1f" % ((a+b)*c / 2))