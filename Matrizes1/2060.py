n = int(input())
l = list(map(int, input().split()))

mult2 = 0
mult3 = 0
mult4 = 0
mult5 = 0

for i in range(n):

    if l[i] % 2 == 0:
        mult2 += 1

    if l[i] % 3 == 0:
        mult3 +=1

    if l[i] % 4 == 0:
        mult4 +=1 

    if l[i] % 5 == 0:
        mult5 +=1
        
print("%d Multiplo(s) de 2" % mult2)   
print("%d Multiplo(s) de 3" % mult3)     
print("%d Multiplo(s) de 4" % mult4)
print("%d Multiplo(s) de 5" % mult5)