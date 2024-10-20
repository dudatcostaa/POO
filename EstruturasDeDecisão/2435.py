n1, d1, v1 = input().split()
n2, d2, v2 = input().split()

n1 = int (n1)
d1 = int (d1)
v1 = int (v1)
n2 = int (n2)
d2 = int (d2)
v2 = int (v2)

if (d1 / v1) < (d2 / v2):
    print("%d" % n1)
else:
    print("%d" % n2)