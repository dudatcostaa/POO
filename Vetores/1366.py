while True:
    
    n = int(input())
    
    if n == 0:
        break
    
    quantidadePares = 0
    for i in range (n):
        ci, vi = input().split()
        ci = int(ci)
        vi = int(vi)
        
        if vi % 2 == 1:
            vi -= 1 
            
        quantidadePares += vi
        
    print(quantidadePares // 4) 