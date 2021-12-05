def convertFloat(number):
    return float(number)

n1, n2, n3, n4 = map(convertFloat, input().split())

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10.0

print("Media: %.1f" %media)

if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")

    ne = float(input())

    print("Nota do exame: %.1f" %ne)

    media = (media + ne) / 2

    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print("Media final: %.1f" %media)