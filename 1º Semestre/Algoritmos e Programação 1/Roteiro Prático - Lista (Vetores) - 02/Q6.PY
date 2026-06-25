import random

def jogo_adivinhacao():
    # Gera uma lista de números aleatórios entre 1 e 100
    quantidade_numeros = 2  # Quantos números a lista terá
    numeros = random.sample(range(1, 101), quantidade_numeros)
    tentativas_maximas = 10  # Número máximo de tentativas

    print(f"Bem-vindo ao jogo de adivinhação! Você precisa adivinhar {quantidade_numeros} números.")
    print(f"Você tem {tentativas_maximas} tentativas para adivinhar cada número.")

    for i, numero in enumerate(numeros):
        print(f"\nAdivinhe o {i+1}º número (entre 1 e 100):")
        tentativas = 0
        adivinhado = False

        while tentativas < tentativas_maximas and not adivinhado:
            tentativa = int(input("Digite sua tentativa: "))  # Sem verificação de entrada
            tentativas += 1

            if tentativa == numero:
                print(f"Parabéns! Você adivinhou o número {numero} em {tentativas} tentativas.")
                adivinhado = True
            elif tentativa < numero:
                print(f"O número é maior que {tentativa}.")
            else:
                print(f"O número é menor que {tentativa}.")
        
        if not adivinhado:
            print(f"Você não conseguiu adivinhar o número. O número correto era {numero}.")
    
    print("\nFim de jogo! Obrigado por jogar.")

# Inicia o jogo
jogo_adivinhacao()
