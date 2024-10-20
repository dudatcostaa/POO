pulo, canos = map(int, input().split())

altura = list(map(int, input().split()))

win = True

for i in range(canos - 1):
    if abs(altura[i] - altura[i + 1]) > pulo:
        win = False
        break
    
if win:
    print("YOU WIN")
else:
    print("GAME OVER")