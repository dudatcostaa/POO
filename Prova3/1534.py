while True:
    try:
        n = int(input())

        while n > 0:
            valor = ""

            for i in range(1, n + 1):
                linha = ""
                for j in range(1, n + 1):
                    if i + j == n + 1:
                        linha += '2'
                    elif i == j:
                        linha += '1'
                    else:
                        linha += '3'
                valor += linha + "\n"    
            print(valor, end = "")
            n = int(input())       
                 
    except EOFError:
        break


while True:
    try:
        entrada = int(input()) 
        while entrada > 0:
            valor = ""
            for i in range(1, entrada + 1):
                linha = ""
                for j in range(1, entrada + 1):
                    if i + j == entrada + 1:
                        linha += '2'
                    elif i == j:
                        linha += '1'
                    
                    else:
                        linha += '3'
                valor += linha + "\n"
            print(valor, end = '') 
            entrada = int(input()) 
    except EOFError:
        break

