while True:
    try:
        n = int(input())
        x = "" #traducao

        for _ in range(n):
            bin = input().strip()

            dec = 0 #inicio o número decimal em 0
            multiplicador = 1

            for i in range(len(bin)-1, -1, -1): #lendo a string da direita para a esquerda
                if bin[i] == '1': #se meu dígito atual for 1, devo somar o multiplicador atual no meu número decimal
                    dec += multiplicador

                multiplicador *= 2 #a cada deslocamento para a esquerda seu peso muda
            x += chr(dec) #chr transforma valores decimais em ASCII

        print(x)
    except EOFError:
        break    