N = int(input())

coposquebrados = 0

for i in range(N):
    l, c = input().split()
    l = int(l)
    c = int(c)
    if l > c:
        coposquebrados += c

print(coposquebrados)