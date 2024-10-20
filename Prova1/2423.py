a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

d = a // 2
e = b // 3
f = c // 5

if d <= e and d <= f:
    maxbolos = d 
elif e <= d and e <= f:
    maxbolos = e
else:
    maxbolos = f 
    
print(maxbolos)