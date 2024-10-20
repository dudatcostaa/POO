while True:
    
    p, n, c = input().split()
    p = int(p)
    n = int(n)
    c = int(c)
    
    if p == 0 and n == 0 and c == 0:
        break
    
    qtpalitos = 0
    comp = [0] * p 
    
    for _ in range(n):
        medicoes = input().split()
    
        for i in range(p):
            medicoes[i] = int(medicoes[i])
            
            if medicoes[i] == 0:
                if comp[i] >= c:
                    qtpalitos += 1 
                comp[i] = 0
            else:
                comp[i] += 1
            
    for i in range(p):
        if comp[i] >= c:
            qtpalitos+= 1 
            
    print(qtpalitos)