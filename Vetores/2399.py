n = int(input())
x = []

for i in range (n):
    x.append(int(input()))

total_bombas = [0] * n #lista que vai armazenar o total de bombas na vizinhanca

for i in range(n):
    bombas = 0 #iniciando as bombas em 0
    if x[i] == 1:
        bombas += 1
    if i > 0 and x[i - 1] == 1:
        bombas += 1
    if i < n-1 and x[i + 1] == 1:
        bombas += 1    

    total_bombas[i] = bombas

for bombas in total_bombas:
    print(bombas)
