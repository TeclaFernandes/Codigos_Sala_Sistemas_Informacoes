# Questão 1:
produtos = ['pastel', 'caldo de cana', 'baião cremoso', 'mungunzá', 'feijoada']

# Questão 2:
terceiro_item = produtos[2]
print(terceiro_item)

# Questão 3:
tamanho_lista = len(produtos)
for c in range(tamanho_lista):
    print(produtos[c], '- ', end="")

# Questão 4:
indice = 0
while (indice < tamanho_lista):
    print(produtos[indice], '- ', end="")
    indice += 1

# Questão 5:
print(tamanho_lista)

# Questão 6:
print(f'ultimo: {produtos[tamanho_lista-1]} e penultimo: {produtos[tamanho_lista-2]}')

# Questão 7:
produtos.append('coca-cola')
produtos.append('cajuína são geraldo')
produtos.append('guaraná kuat')

# Questão 8:
produtos.pop(1)
print(produtos)

# Questão 9:
tamanho_lista_novo = len(produtos)
item = 'coca-cola'
print(tamanho_lista_novo)
for c in range(tamanho_lista_novo-1, -1, -1):
    if item == produtos[c]:
        produtos.pop(c)
print(produtos)

# Questão 10:
ordem_alfabetica = sorted(produtos)
print(ordem_alfabetica)

# Questão 11:
outros_produtos = []
outros_produtos.append('leite')
outros_produtos.append('tapioca')
# produtos.extend(outros_produtos)
produtos += outros_produtos

# Questão 12:
nova_lista = produtos[1:4]
print(nova_lista)

# Questão 13:
outra_lista = produtos[3:]
print(outra_lista)

# Questão 14:
print(produtos[:5])

# Questão 15: 
produtos[1] = 'celular'
print(produtos)