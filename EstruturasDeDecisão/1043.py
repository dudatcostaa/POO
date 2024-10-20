a, b, c = input() .split()
a = float(a)
b = float(b)
c = float(c)

if a + b > c and a + c > b and b + c > a:
    print("Perimetro = %.1f" % (a + b + c))
else:
    area = ((a + b) * c) / 2
    print("Area = %.1f" % area)