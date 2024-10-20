codificada = input()

decodificada = ""
i = 0

while i  < len(codificada):
    if codificada[i] == 'p':
        decodificada += codificada[i + 1]
        i += 2
    else: #caso o próximo index for um espaço em branco, ele não é um P então devemos manter ele
        decodificada += codificada[i]
        i += 1
            