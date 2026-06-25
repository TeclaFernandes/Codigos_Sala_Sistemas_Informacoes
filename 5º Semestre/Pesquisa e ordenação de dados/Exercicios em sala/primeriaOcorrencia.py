def BuscaBinariaRecursiva(lista, alvo, inicio, fim):
    if inicio > fim:
        return -1 
    
    # meio = int((inicio + fim) / 2)
    meio = int(fim + (inicio + fim) / 2)

    if lista[meio] == alvo:
        return meio
    elif lista[meio] < alvo:
        return BuscaBinariaRecursiva(lista, alvo, meio + 1, fim)
    else: 
        return BuscaBinariaRecursiva(lista, alvo, inicio, meio - 1)
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alvo = 7
inicio = 1
fim = 8
print(BuscaBinariaRecursiva(lista, alvo, inicio, fim))