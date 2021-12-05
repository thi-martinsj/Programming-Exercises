cedulas = [100,50,20,10,5,2,1]

number = int(input())

print(str(number))

aux = number

for i in range(len(cedulas)):

    qtd = int(aux / cedulas[i])
    aux = aux % cedulas[i]

    print(f"{qtd} nota(s) de R$ {cedulas[i]},00")