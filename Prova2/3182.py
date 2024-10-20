p, o, h, s = list(map(int,input().split()))

final = set()
stayhome = True

for _ in range (h):
    preco = int(input())
    camas = list(map(int, input().split()))
        
    for i in range(s):
        if camas[i] > p:
            total = p*preco
            
            if total <= o:
                final.add(total)
                stayhome = False
                
if stayhome:
    print("stay home")
    
else:
    print(min(final))