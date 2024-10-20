x = input().split()
y = input().split()

encaixa = True

for i in range(0, 5):
    x[i] = int(x[i])
    y[i] = int(y[i])
    
    if x[i] == y[i]:
        encaixa = False
        break
    
if encaixa:
    print('Y')
else:
    print('N')