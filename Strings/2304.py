i, n = input().split()

i = int(i)
n = int(n)

D = i
E = i
F = i

for _ in range (n):
    ni = input().split()
    
    if ni[0] == "C":
        valor = int(ni[2])
        if ni[1] == "D":
            D -= valor
        
        elif ni[1] == "E":
            E -= valor
        
        else:
            F -= valor
    
    elif ni[0] == "V":
        valor = int(ni[2])
        if ni[1] == "D":
            D += valor
        
        elif ni[1] == "E":
            E += valor
        
        else:
            F += valor
    
    elif ni[0] == "A":
        valor = int(ni[3])
        if ni[1] == "D" and ni[2] == "E":
            D += valor
            E -= valor
        
        elif ni[1] == "D" and ni[2] == "F":
            D += valor
            F -= valor
        
        elif ni[1] == "E" and ni[2] == "D":
            E += valor
            D -= valor
        
        elif ni[1] == "E" and ni[2] == "F":
            E += valor
            F -= valor
        
        elif ni[1] == "F" and ni[2] == "D":
            F += valor
            D -= valor
        
        elif ni[1] == "F" and ni[2] == "E":
            F += valor
            E -= valor

print (D, E, F)