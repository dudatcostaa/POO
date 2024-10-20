q = int(input())
votos = input().split()

s = 0
ns = 0

for i in votos:
    
    if i == '0':
        s += 1
    else:
        ns +=1
        
if s > ns:
    print("Y")
else:
    print("N")