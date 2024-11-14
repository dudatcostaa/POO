matriz = [None] * 3
for i in range(3):
    matriz[i] = list(map(int, input().split()))

soma = None    

for linha in matriz:
    if 0 not in linha:
        soma = sum(linha)
        break

for i in range(3):
    for j in range(3):
            matriz[i][j] == 0:
                matriz[i][j] = soma - sum(matriz[i])

for linha in matriz:
     print(*linha)            
