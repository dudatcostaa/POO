c = int(input())

for _ in range(0, c):
    n = input().split()
    for i in range(0, len(n)):
        n[i] = int(n[i])
    
    soma = 0    
    
    for i in range(1, len(n)):
        soma += n[i]
    
    media = soma / n[0]
    
    acima = 0
    
    for i in range (1, len(n)):
        if n[i] > media:
            acima += 1
            
    percentual = acima / n[0]  * 100    
       
    print("%.3f%%" % percentual)