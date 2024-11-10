def min(a, b, c, d): #funcao para descobrir o mínimo entre 4 valores
    x = a
    if b < x:
        x = b
    if c < x:
        x = c
    if d < x:
        x = d
    return x

mat = [None] * 100 #criando a matriz
for i in range(100):
    mat[i] = [None] * 100

while True:
    n = int(input())
    if n==0:
        break

#a menor distância de cada casa [] até a borda, define o número    
#(i + 1) define a distância até a borda superior
#(j + 1) define a distância até a borda esquerda
#(n - i) define a distância até a borda inferior
#(n - j) define a distância até a borda direita
#usando a funcao min descobrimos a menor distancia da casa até alguma borda

    for i in range(n):
        for j in range(n):
            mat[i][j] = min(i + 1, j + 1, n - i, n - j)

    for i in range(n):
        print ("%3d" % mat[i][j], end='')
        for j in range(1, n):
            print (" %3d" % mat[i][j], end='')
        print()
    print()