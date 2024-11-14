o = input()

matriz = [None] * 12

for i in range (0,12):
    matriz[i] = [None] * 12

for i in range (0,12):
    for j in range (0,12):
        matriz[i][j] = float(input())

soma = 0

for i in range (6,12):
    for j in range (12-i,i):
        soma += matriz[i][j]

if o == 'S':
    print("%.1f" % (soma))
else:
    print("%.1f" % (soma / 30))