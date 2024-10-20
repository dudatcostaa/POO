v = int(input())
p = int(input())

x = v / p

r = v % p 

for i in range(0, p):
    if i < r:
        print("%d" % (x + 1))
    else:
        print("%d" % x)