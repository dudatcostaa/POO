n = int(input())

linha = input().split()

while n > 1: #enquanto houver mais que uma bolinha
    superior = [] #armazenar as bolinhas na lonha superior
    for i in range (n-1):
        if linha[i] == linha [i+1]: #bolinhas da mesma cor
            superior.append('1') #adiciono bolinha preta na linha superior
        else:
            superior.append('-1') #adiciono bolinha branca na linha superior
    linha = superior #linha superior se torna a atual
    n -= 1 #com uma bolinha a menos

if linha [0] == '1':
    print("preta")
else:
    print("branca")    