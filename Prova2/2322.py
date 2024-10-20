n = int(input())
pecas = list(map(int,input().split()))

numeros = list(range(1, n + 1))

for i in numeros:
    if i not in pecas:
        print(i)