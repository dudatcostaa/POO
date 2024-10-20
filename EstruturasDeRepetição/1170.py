testes = int(input())

for _ in range(testes):
    comida = float(input())
    dias = 0
    
    while comida > 1:
        comida /= 2
        dias += 1
        
    print("%d dias" % dias)