n, l, d = input().split()
n = int(n)
l = int(l)
d = int(d)

litrospedidos = (n * d) / 1000

if litrospedidos % l == 0:
    litrosminimo = int(litrospedidos)
else:
    litrosminimo = (int(litrospedidos / l) + 1) * l
    
print("%d" % litrosminimo)