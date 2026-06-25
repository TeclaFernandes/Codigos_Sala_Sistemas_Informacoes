def desenhar_piramide(altura):
    for i in range(altura):
        # Espaços em branco à esquerda
        espacos = ' ' * (altura - i - 1)
        # Asteriscos
        asteriscos = '*' * (2 * i + 1)
        # Desenha a linha da pirâmide
        print(espacos + asteriscos)

# Solicita a altura da pirâmide ao usuário
altura = int(input("Digite a altura da pirâmide: "))
desenhar_piramide(altura)
