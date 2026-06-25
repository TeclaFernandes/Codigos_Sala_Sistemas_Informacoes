# Versão 2

lista = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]

menor = lista[0]
indice_menor = 0

for c in range(len(lista)):
    if lista[c] < menor:
        menor = lista[c]
        indice_menor = c

subLista = lista[indice_menor:]
maior = subLista[0]
indice_maior = 0

for i in range(len(subLista)):
    if subLista[i] > maior:
        maior = subLista[i]
        indice_maior = i + indice_menor

print('Melhor dia de Compra: ', indice_menor)
print('Melhor dia de Venda: ', indice_maior)
