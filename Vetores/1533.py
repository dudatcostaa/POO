while True:
    n = int(input())
    if n == 0:
        break
    
    s = input().split()
    mais = int(s[0])
    segundo = 0
    posmais = 0
    possegundo = 0
    
    for i in range(1, n):
        
        s[i] = int(s[i])
        
        if s[i] > mais:
            segundo = mais
            mais = s[i]
            
            possegundo = posmais
            posmais = i
        elif s[i] > segundo:
            possegundo = i
            
            segundo = s[i]
            
    possegundo += 1        
    print(possegundo)