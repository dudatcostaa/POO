while True:
    try:
        linha, coluna = input().split()
        linha = int(linha)
        coluna = int(coluna)

        matriz = [None] * n
        for i in range(n):
            matriz[i] = input().split()
            matriz[i][j] = int(matriz[i][j])

            total = 0

            for i in range(linha):
                for j in range(coluna):
                    total += matriz[i][j]

            sacas = total // 60 #divisao arredondada pra baixo
            litros = total % 60 #resto     

            print("%d saca(s) e %d litro(s)" % sacas, litros)  

    except EOFError:
        break
