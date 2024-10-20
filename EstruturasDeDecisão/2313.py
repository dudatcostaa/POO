a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a + b <= c or b + c <= a or a + c <= b:
    print("Invalido")
else:
    if a == b == c:
        print("Valido-Equilatero")
    elif a == b or a == c or b == c:
        print("Valido-Isoceles")
    else:
        print("Valido-Escaleno")
    
    if (a ** 2 == b ** 2 + c ** 2) or (b ** 2 == a ** 2 + c ** 2) or (c ** 2 == a ** 2 + b ** 2):
        print("Retangulo: S")
    else:
        print("Retangulo: N")