while True:
    try:
        n, m = input().split() #n postos, m dist atleta consegue
        n = int(n)
        m = int(m)

        p = list(map(int, input().split())) # metros postos de água

        p.append(42195) #adicionando a linha de chegada

        resultado = "S"

        for i in range(1, n + 1):
            if p[i] - p[i] > m:
                resultado = "N"
                break

        print(resultado)    

    except EOFError:
        break

    #deu runtime error