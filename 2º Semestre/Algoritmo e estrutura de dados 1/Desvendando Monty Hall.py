# Leitura do número de jogos
N = int(input())

# Contador de vitórias
cont = 0

# Simulação dos jogos
for i in range(N):
    porta_carro = int(input())  # Porta onde o carro está
    if porta_carro != 1:  # O jogador ganha se o carro NÃO estiver na porta 1
        cont += 1

# Resultado final
print(cont)
