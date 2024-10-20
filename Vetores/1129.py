while True:
    n = int(input())
    if n == 0:
        break
        
    for _ in range (0, n):
        v = input().split()
        respostas = 0
        marcada = 0
        
        for i in range(0, len(v)):
            v[i] = int(v[i])
            
            if v[i] <= 127:
                respostas += 1 
                marcada = i
        
        if respostas == 1:
            if marcada == 0:
                print('A')
            elif marcada == 1:
                print('B')
            elif marcada == 2:
                print('C')
            elif marcada == 3:
                print('D')
            else:
                print('E')
        
        else:
            print('*')