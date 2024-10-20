n = int(input())

x = input().split()
menorvalor = int(x[0])
posicao = 0

for i in range (0, n):

    x[i] = int(x[i])
    
    if x[i] < menorvalor:
        menorvalor = x[i]
        posicao = i
    
print("Menor valor: %d" % menorvalor)
print("Posicao: %d" % posicao)