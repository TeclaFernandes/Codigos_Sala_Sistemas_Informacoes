# Versão 1

lista = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]

menor = lista[0]

for c in lista:
    if menor > c:
        menor = c

subLista = lista[lista.index(menor):]
maior = subLista[0]

for i in subLista:
    if maior < i:
        maior = i

print('Melhor dia de Compra: ', lista.index(menor))
print('Melhor dia de Venda: ', lista.index(maior))