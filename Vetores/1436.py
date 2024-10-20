t = int(input())
teste = 0

for _ in range (0, t):
    teste += 1 
    
    n = input().split()
    n[0] = int(n[0])
    
    l = (n[0] // 2) + 1
    
    print("Case %d: %d" % (teste, int(n[l])))