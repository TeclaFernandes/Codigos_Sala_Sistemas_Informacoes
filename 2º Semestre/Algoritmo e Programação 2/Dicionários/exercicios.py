# item a
pessoas = {'Ana': 25, 'Carlos': 30, 'Beatriz': 22}
print(pessoas)

# Item b 
pessoas['Jose'] = 55
print(pessoas)

# Item c
del pessoas['Ana']
print(pessoas)

# Item d
for k, v in pessoas.items():
    print(f'Nome: {k}, Idande: {v}')

# Item e
print(pessoas.get('Tecla', 'Erro... chave não existe...'))

# Item f
print(len(pessoas))

# Item g
print(pessoas.keys())

# Item h
def adicionar_pessoas(lista_nomes, lista_idades):
    if len(lista_nomes) != len(lista_idades):
        print("Erro: As listas de nomes e idades devem ter o mesmo tamanho.")
        return None

    return {nome: idade for nome, idade in zip(lista_nomes, lista_idades)}
print(adicionar_pessoas(['João', 'Diego', 'Daniel', 'Will'], [22, 31, 25, 19]))

# Item i
def incrementa_idades(lista_nomes, lista_idades):
    dicionario = adicionar_pessoas(lista_nomes, lista_idades)
    if not dicionario:
        return

    for nome, idade in dicionario.items():
        print(f'Nome: {nome}, Idade: {idade + 1}')

incrementa_idades(['João', 'Diego', 'Daniel', 'Will'], [22, 31, 25, 19])

# Item j
def somar_idades(dicionario):
    return sum(dicionario.values())

dicionario = {'João': 22, 'Diego': 31, 'Daniel': 25, 'Will': 19}

soma = somar_idades(dicionario)
print(f"Soma das idades: {soma}")

# Item k 
def remover_pessoas_por_idade(dicionario, idade_minima):
    return {nome: idade for nome, idade in dicionario.items() if idade >= idade_minima}

dicionario = {'João': 22, 'Diego': 31, 'Daniel': 25, 'Will': 19}

idade_minima = 25
novo_dicionario = remover_pessoas_por_idade(dicionario, idade_minima)
print(f"Novo dicionário: {novo_dicionario}")

# Item l
cidades = {"Farias Brito": 12300000, "Varzea Alegre": 6748000, "Crato": 2872000}

cidades["Juazeiro do Norte"] = 2523000
cidades["Fortaleza"] = 1484000
cidades["Recife"] = 12400000

del cidades["Recife"]
print("Dicionário atualizado:", cidades)

# Item m
def encontrar_maior_idade(dicionario):
    nome_mais_velho = max(dicionario, key=dicionario.get)
    return nome_mais_velho, dicionario[nome_mais_velho]

pessoas = {"João": 22, "Diego": 31, "Daniel": 25, "Will": 19}

nome, idade = encontrar_maior_idade(pessoas)
print(f"A pessoa mais velha é {nome} com {idade} anos.")

# Item n
def calcular_media(dicionario):
    return {nome: sum(notas) / len(notas) for nome, notas in dicionario.items()}

notas = {
    "João": [7.5, 8.0], "Maria": [9.0, 8.5], "Carlos": [6.0, 7.0, 8.0]}

medias = calcular_media(notas)
print("Médias das notas:", medias)

# Item o
estoque = {
    "Arroz": {"preço": 5.50, "quantidade": 10},
    "Feijão": {"preço": 8.00, "quantidade": 15},
    "Açúcar": {"preço": 4.20, "quantidade": 20}}

estoque["Óleo"] = {"preço": 6.50, "quantidade": 12}
estoque["Leite"] = {"preço": 4.00, "quantidade": 30}
estoque["Macarrão"] = {"preço": 3.75, "quantidade": 25}

def atualizar_estoque(estoque, produto, quantidade):
    if produto in estoque:
        estoque[produto]["quantidade"] += quantidade
        if estoque[produto]["quantidade"] < 0:
            estoque[produto]["quantidade"] = 0
    else:
        print(f"Produto '{produto}' não encontrado no estoque.")

def calcular_valor_total_estoque(estoque):
    return sum(info["preço"] * info["quantidade"] for info in estoque.values())

atualizar_estoque(estoque, "Arroz", 5)
atualizar_estoque(estoque, "Óleo", -3) 
print("Estoque atualizado:", estoque)

valor_total = calcular_valor_total_estoque(estoque)
print(f"Valor total do estoque: R$ {valor_total:.2f}")
