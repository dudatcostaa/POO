n = int(input())
for _ in range(0,n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    
    if x > y:
        t = x 
        x = y 
        y = t
    
    if x % 2 == 0:
        x += 1
    else:
        x += 2
        
    if y % 2 == 0:
        y -= 1 
    else:
        y -= 2
    
    soma = 0
    for i in range(x, y + 1, 2):
        soma += i 
    print(soma)
     # sn = (x + y) * (y - x + 1) // 2