itens, bolinhos = list(map(int,input().split()))

natan = list(map(int,input().split()))
samuel = list(map(int,input().split()))

qtbolinhosnatan = natan.count(1)
qtbolinhossamuel = samuel.count(1)

if qtbolinhosnatan == bolinhos:
    print ("Tudo certo.")
    
elif qtbolinhosnatan != bolinhos and qtbolinhossamuel == bolinhos:
    print ("Pegou de Samuel.")
    
else:
    print ("Pegou de um estranho.")