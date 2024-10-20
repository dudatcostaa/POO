m = int(input())
a = int(input())
b = int(input())

x = a + b
c = m - x 

if a > c and a > b:
    print("%d" % a)
elif b > a and b > c:
    print("%d" % b)
else:
    print("%d" % c)