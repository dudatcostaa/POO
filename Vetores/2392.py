n, m = input().split()

n = int(n)
m = int(m)

pedras = [0] * (n + 1)

for _ in range(m):
    p, d = input().split()
    p = int(p)
    d = int(d)
    
    for x in range(p, n + 1, d):
        pedras[x] = 1 
        
    for x in range(p, 0, -d):
        pedras[x] = 1 
        
for i in range(1, n + 1):
    print(pedras[i])