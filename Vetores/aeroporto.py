teste = 1
voos = [None] * 101
while True:
    a, v = input().split() #a=aeroportos v=voos
    a = int(a) 
    v = int(v)

    if a == 0 and v == 0:
        break

    for i in range(1, a + 1): #inicializando os aeroportos em 0
        voos[i] = 0

    for i in range(v):
        x, y = input().split() #voo vai de um aeroporto x e chega no aeroporto y
        x = int(x)
        y = int(y)

        voos[x] += 1 #somo 1 no aeroporto x
        voos[y] += 1 #somo 1 no aeroporto y

    mais_congestionado = 0
    for i in range(1, a + 1):
        if voos[i]> mais_congestionado:
            mais_congestionado = voos[i]

    print("Teste %d" % teste) #imprimo o número do caso teste

    for i in range(1, a + 1):
        if voos[i] == mais_congestionado:
            print("%d " % i, end='')
    print()
    print()
    teste = +1