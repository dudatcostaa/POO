a, b, c, d = input() .split()
a = float(a)
b = float(b)
c = float(c)
d = float(d)

if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")