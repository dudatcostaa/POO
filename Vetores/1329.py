while True:
    n = int(input())
    if n == 0:
        break
    
    r = input().split()
    maria = 0
    joao = 0
    
    for i in range(0, len(r)):
        r[i] = int(r[i])
        
        if r[i] == 0:
            maria += 1
        else:
            joao += 1 
            
    print(f"Mary won {maria} times and John won {joao} times")s