linha1 = list(map(int,input().split()))
linha2 = list(map(int,input().split()))

quantosacertou = 0 

for i in linha1:
    if i in linha2:
        quantosacertou += 1

if quantosacertou == 3:
    print("terno")
    
elif quantosacertou == 4:
    print("quadra")
    
elif quantosacertou == 5:
    print("quina")
    
elif quantosacertou == 6:
    print("sena")
    
elif quantosacertou < 3:
    print("azar")