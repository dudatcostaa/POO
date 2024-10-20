n = int(input())

verbas = 0
gastos = 0

for _ in range(0, n):
    v, c = input().split()
    c = int(c)
    
    if v == "G":
        gastos += c 
    elif v == "V":
        verbas += c 

if gastos > verbas:
    print("NAO VAI TER CORTE, VAI TER LUTA!")
else:
    print("A greve vai parar.")