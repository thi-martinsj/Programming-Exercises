a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

delta = b**2 - 4 * a * c

try:

    r1 = (-b + (delta ** (1/2))) / (2 * a)
    r2 = (-b - (delta ** (1/2))) / (2 * a)

    print("R1 = %.5f" %r1)
    print("R2 = %.5f" %r2)

except:
    print("Impossivel calcular")