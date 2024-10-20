n = int(input())

mensagem = input().split()
    
for hexa in mensagem:
    m = int(hexa, 16)
    alfabeto = chr(m)
    print(alfabeto, end="")
    
print()