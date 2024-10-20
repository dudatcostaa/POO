n = int(input())

for _ in range(0, n):
    cripto = input()
    
    correto = list(cripto)
    
    for i in range(len(cripto)-1, -1, -1):
        if  correto[i].islower():
            print(correto[i], end = "")
    print()