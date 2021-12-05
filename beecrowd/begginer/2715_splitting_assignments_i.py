while True:

    try:

        n = int(input())

        elements = []

        elements = list(map(int, input().split()))

        r = 0
        g = 0

        i = 0
        j = n - 1

        if len(elements) > 1:

            while i <= j:

                if (r + elements[i]) <= (g + elements[j]):
                    r += elements[i]
                    i += 1

                else:
                    g += elements[j]
                    j -= 1

            dif = abs(r - g)

        else:
            dif = elements[0]


        print("%d" % dif)

    except EOFError:
        break