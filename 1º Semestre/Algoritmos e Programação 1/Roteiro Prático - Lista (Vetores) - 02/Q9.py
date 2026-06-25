# Listas para armazenar eleitores e os respectivos bairros
bairros = ['Centro', 'Seminario', 'Pimenta']
eleitores = []
bairros_associados = []

# Função para adicionar eleitores ao bairro
def adicionar_eleitor(numero, bairro):
    if bairro in bairros:
        eleitores.append(numero)
        bairros_associados.append(bairro)
    else:
        print("Bairro inválido! Escolha entre Centro, Seminário ou Pimenta.")

# Loop para coletar dados de eleitores
numero = input("Digite o número do eleitor (ou ENTER para encerrar): ")
while numero != '':  # Continua até o usuário pressionar ENTER
    bairro = input("Digite o bairro (Centro, Seminário, Pimenta): ").capitalize()
    adicionar_eleitor(numero, bairro)
    numero = input("Digite o número do eleitor (ou ENTER para encerrar): ")

# Quantidade total de eleitores participantes
total_eleitores = len(eleitores)
print(f"\nTotal de eleitores participantes: {total_eleitores}")

# Exibir lista de eleitores por bairro
for bairro in bairros:
    eleitores_do_bairro = [eleitores[i] for i in range(len(eleitores)) if bairros_associados[i] == bairro]
    print(f"Eleitores do bairro {bairro}: {eleitores_do_bairro}")

# Encontrar o bairro com o maior número de eleitores
maior_numero = 0
bairro_mais_popular = ""

for bairro in bairros:
    numero_de_eleitores = sum(1 for b in bairros_associados if b == bairro)
    
    if numero_de_eleitores > maior_numero:
        maior_numero = numero_de_eleitores
        bairro_mais_popular = bairro

print(f"\nO bairro com o maior número de eleitores é: {bairro_mais_popular}")

# Permitir pesquisa de um eleitor específico
numero_pesquisado = input("\nDigite o número do eleitor para buscar (ou ENTER para encerrar): ")
while numero_pesquisado != '':
    encontrado = False
    for i in range(len(eleitores)):
        if eleitores[i] == numero_pesquisado:
            print(f"O eleitor {numero_pesquisado} vota no bairro {bairros_associados[i]}.")
            encontrado = True

    # Se o eleitor não foi encontrado
    if not encontrado:
        print(f"O eleitor {numero_pesquisado} não foi encontrado na pesquisa.")

    numero_pesquisado = input("\nDigite o número do eleitor para buscar (ou ENTER para encerrar): ")
