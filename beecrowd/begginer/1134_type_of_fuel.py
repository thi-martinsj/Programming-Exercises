combustivel = {
    "Alcool": 0,
    "Gasolina": 0,
    "Diesel": 0
}

value = int(input())

while value != 4:

    if value == 1:
        combustivel["Alcool"] += 1
    elif value == 2:
        combustivel["Gasolina"] += 1
    elif value == 3:
        combustivel["Diesel"] += 1

    value = int(input())

print("MUITO OBRIGADO")
print("\n".join(map(str,combustivel.items())).replace("(", "").replace(")", "").replace("'", "").replace(",", ":"))