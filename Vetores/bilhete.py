while True:
    
    n, m = input().split()
    n = int(n)
    m = int(m)
    
    if n == 0 and m == 0:
        break
    
    bilhetes = input().split()
    contadorCopias = [0] * (n + 1)
    for i in range(m):
        contadorCopias[int(bilhetes[i])] += 1 
    
    falsos = 0
    
    for i in range(n + 1):
        if contadorCopias[i] > 1:
            falsos += 1 
    
    print(falsos)
    