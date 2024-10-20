teste = 1 
while True:
    r = int(input())
    
    if r == 0:
        break
    
    pontosaldo = 0
    pontosbeto = 0
    
    for i in range(r):
        a, b = input().split()
        a = int(a)
        b = int(b)
        
        pontosaldo += a 
        pontosbeto += b 
    
    print("Teste %d" % teste)    
    
    if pontosaldo > pontosbeto:
        print("Aldo")
    else:
        print("Beto")
        
    print() 
    
    teste += 1 