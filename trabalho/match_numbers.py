import random

# Configurações básicas
LINHAS = 5
COLUNAS = 5
TAMANHO_PECA = 3  # Para facilitar o layout no terminal

# Função para criar a grade com números aleatórios
def criar_grade(linhas, colunas):
    return [
        [random.randint(1, 9) for _ in range(colunas)]
        for _ in range(linhas)
    ]

# Função para desenhar a grade e os números no terminal
def desenhar_grade(grade):
    for linha in grade:
        print(" ".join(f"{num:3}" if num != 0 else "  0" for num in linha))
    print("\n")

# Função para verificar se dois números podem ser eliminados
def pode_eliminar(grade, pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    num1 = grade[x1][y1]
    num2 = grade[x2][y2]

    # Verifica se são iguais ou somam 10
    if num1 == num2 or num1 + num2 == 10:
        # Verificar se estão na mesma linha ou coluna
        if x1 == x2:  # Mesmo linha
            return y1 < y2 and all(grade[x1][y] == 0 for y in range(y1 + 1, y2))
        if y1 == y2:  # Mesma coluna
            return x1 < x2 and all(grade[x][y1] == 0 for x in range(x1 + 1, x2))

        # Verificar se estão na diagonal (sem números entre eles)
        if abs(x1 - x2) == abs(y1 - y2):  # Estão na diagonal
            if x1 < x2 and y1 < y2:  # Diagonal crescente
                for i in range(1, abs(x1 - x2)):
                    if grade[x1 + i][y1 + i] != 0:
                        return False
            elif x1 > x2 and y1 > y2:  # Diagonal decrescente
                for i in range(1, abs(x1 - x2)):
                    if grade[x1 - i][y1 - i] != 0:
                        return False
            elif x1 < x2 and y1 > y2:  # Diagonal inversa (crescente nas linhas e decrescente nas colunas)
                for i in range(1, abs(x1 - x2)):
                    if grade[x1 + i][y1 - i] != 0:
                        return False
            elif x1 > x2 and y1 < y2:  # Diagonal inversa (decrescente nas linhas e crescente nas colunas)
                for i in range(1, abs(x1 - x2)):
                    if grade[x1 - i][y1 + i] != 0:
                        return False
            return True
        
        # Verificar a regra de combinar a primeira e a última linha na mesma coluna
        if (x1 == 0 and x2 == LINHAS - 1) or (x2 == 0 and x1 == LINHAS - 1):
            if y1 == y2:
                return True

    return False

# Função para verificar se há combinações possíveis restantes
def ha_combinacoes(grade):
    for x1 in range(LINHAS):
        for y1 in range(COLUNAS):
            if grade[x1][y1] != 0:
                for x2 in range(LINHAS):
                    for y2 in range(COLUNAS):
                        if (x1 != x2 or y1 != y2) and grade[x2][y2] != 0:
                            if pode_eliminar(grade, (x1, y1), (x2, y2)):
                                return True
    return False

# Função principal do jogo
def jogo_number_match():
    grade = criar_grade(LINHAS, COLUNAS)
    fim_de_jogo = False

    while not fim_de_jogo:
        desenhar_grade(grade)

        # Solicitar ao jogador para selecionar duas posições
        try:
            x1, y1 = map(int, input("Escolha o primeiro número (linha, coluna): ").split())
            x2, y2 = map(int, input("Escolha o segundo número (linha, coluna): ").split())

            # Verificar se as posições são válidas
            if not (0 <= x1 < LINHAS and 0 <= y1 < COLUNAS) or not (0 <= x2 < LINHAS and 0 <= y2 < COLUNAS):
                print("Posições inválidas. Tente novamente.")
                continue

            # Verificar se os números podem ser eliminados
            if pode_eliminar(grade, (x1, y1), (x2, y2)):
                print("Os números podem ser combinados!")
                grade[x1][y1] = 0
                grade[x2][y2] = 0
            else:
                print("Esses números não podem ser combinados. Tente novamente.")

        except ValueError:
            print("Entrada inválida. Tente novamente.")

        # Condição de vitória
        if all(num == 0 for linha in grade for num in linha):
            desenhar_grade(grade)
            print("Você venceu! Todos os números foram eliminados.")
            fim_de_jogo = True

        # Verificar se há mais combinações possíveis
        if ha_combinacoes(grade):
            print("Ainda existem combinações possíveis!")
        else:
            # Se o jogador deseja reiniciar
            reiniciar = input("Não há mais combinações possíveis. Deseja reiniciar o jogo? (s/n): ").lower()
            if reiniciar == "s":
                grade = criar_grade(LINHAS, COLUNAS)  # Reinicia o jogo com uma nova grade

# Executa o jogo
jogo_number_match()