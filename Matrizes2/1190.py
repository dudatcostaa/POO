o = input()

mat = [None] * 12
for i in range(12):
    mat[i] = [None] * 12

soma = 0
quantidade = 0   

for i in range(12):
    for j in range(12):
        mat [i][j] = float(input())

        if i < j and i + j > 11: #verifica se está na regiao correta
            soma += mat[i][j] #soma o valor da posicao
            quantidade += 1 #conta o numero de elementos na regiao

if o == 'S':
    print("%1.f" % soma)
else:
    print("%.1f" % soma / quantidade)                
