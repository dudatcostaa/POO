n = input().split()

inicio = n[0]
fim = n[1]

coluna_inicio = ord(inicio[0]) - ord('a') + 1
linha_inicio = int(inicio[1])

coluna_fim = ord(fim[0]) - ord('a') + 1
linha_fim = int(fim[1])

diferenca_coluna = abs(coluna_fim - coluna_inicio)
diferenca_linha = abs(linha_fim - linha_inicio)

if (diferenca_coluna == 2 and diferenca_linha == 1) or (diferenca_coluna == 1 and diferenca_linha == 2):
    print("Movimento válido")
else:
    print("Movimento inválido")
