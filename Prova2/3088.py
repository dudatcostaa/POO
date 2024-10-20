while True:
    try:
        texto = input()

        texto = texto.replace(" ,", ",")

        texto = texto.replace(" .", ".")

        print(texto)

    except EOFError:
        break    
