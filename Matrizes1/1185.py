o = input()

mat = [None] * 12
for i  in range (0, 12):
    mat[i] = [None] * 12
    
for i in range (0, 12):
    for j in range (0, 12):
        mat[i][j] = float(input())
        
soma = 0
quantidade = (144 - 12) / 2

for i in range (0, 12):
    for j in range(0, 12-i-1):  #os quadradinhos verde da linha
        soma += mat[i][j]
    
if o == 'S':
    print("%.1f" % soma)
else:
    print("%.1f" % (soma / quantidade))