import math


def distancia(x1, x2, y1, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


t = int(input())

magic = {
    "fire": {
        "Dano": 200,
        "1": 20,
        "2": 30,
        "3": 50
    },
    "water": {
        "Dano": 300,
        "1": 10,
        "2": 25,
        "3": 40
    },
    "earth": {
        "Dano": 400,
        "1": 25,
        "2": 55,
        "3": 70
    },
    "air": {
        "Dano": 100,
        "1": 18,
        "2": 38,
        "3": 60
    }
}

for i in range(t):

    w, h, x0, y0 = input().split()
    m, n, cx, cy = input().split()

    w = int(w)
    h = int(h)
    x0 = int(x0)
    y0 = int(y0)
    cx = int(cx)
    cy = int(cy)

    InimXFinal = x0 + w
    InimYFinal = y0 + h

    raio = magic[m][n]

    MagiaXIn = cx - raio
    MagiaXFinal = cx + raio
    MagiaYIn = cy - raio
    MagiaYFinal = cy + raio

    # verificando a posição X do centro da bomba em relação ao quadrado inimigo
    if cx > (x0 + w):  # direita
        lado = 'right'
    elif cx < x0:  # esquerda
        lado = 'left'
    else:
        lado = 'between'

    # verificando a posição Y do centro da bomba em relação ao quadrado inimigo
    if y0 >= 0:
        if cy > (y0 + h):
            altura = 'above'
        elif cy < y0:
            altura = 'below'
        else:
            altura = 'between'
    else:
        if cy > y0:
            altura = 'above'
        elif cy < (y0 - h):
            altura = 'below'
        else:
            altura = 'between'

    res = 0
    # calcula a distância entre os pontos mais próximos
    # se for menor igual que o raio é porque atinge
    if lado == 'right':
        y2 = 0

        if altura == 'above':
            y2 = InimYFinal

        elif altura == 'below':
            y2 = y0

        else:
            y2 = cy

        d = distancia(cx, InimXFinal, cy, y2)

    elif lado == 'left':
        y2 = 0

        if altura == 'above':
            y2 = InimYFinal

        elif altura == 'below':
            y2 = y0

        else:
            y2 = cy

        d = distancia(cx, x0, cy, y2)
    else:

        y2 = 0

        if altura == 'above':
            y2 = InimYFinal

        elif altura == 'below':
            y2 = y0

        else:
            y2 = cy

        d = distancia(cx, cx, cy, y2)

    if d <= raio:
        res = magic[m]["Dano"]

    print(res)